import openslide
from PIL import Image
import os
import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("C:/Venky/cancer_ml_project/runs/classify/train/weights/best.pt")  # load a custom model

# Just one side creates 1000s of images. 
# Most of these are just background images and have no value.

image_path='C:\Venky\cancer_ml_project\svs_images\MML\MSB-00140-03-01.svs'
# image_path='C:\Venky\cancer_ml_project\svs_images\LCA\MSB-00122-02-04.svs'

slide = openslide.OpenSlide(image_path)

slide_width, slide_height = slide.dimensions # Get dimensions of the highest resolution level

patch_size = 250 # Desired size of each small image
level = 0

patches_generated_count = 0
background_threshold = 0.8

lung_cancer_counter = 0
multiple_myeloma_counter = 0

for y in range(0, slide_height, patch_size):
    for x in range(0, slide_width, patch_size):
        # Adjust width and height for potential edge cases (last patch might be smaller)
        current_width = min(patch_size, slide_width - x)
        current_height = min(patch_size, slide_height - y)

        if current_width > 0 and current_height > 0: # Ensure valid patch
            patch = slide.read_region((x, y), level, (current_width, current_height))
            patch_np = np.array(patch)

            # Convert to grayscale to detect background.
            gray = np.mean(patch_np, axis=2) / 255.0 # Normalize to [0,1]
            white_pixels = np.sum(gray > 0.9)
            total_pixels = patch_size * patch_size
            white_ratio = white_pixels / total_pixels

            if ( white_ratio < background_threshold ):
                if patch.mode != 'RGB':
                    patch = patch.convert('RGB')

                #Predict what cancer this patch might have.
                result = model.predict(patch)
                probs_object = result[0].probs
                probabilities = probs_object.data.cpu().numpy()
                if(probabilities[0] > 0.8):
                    lung_cancer_counter = lung_cancer_counter + 1

                if(probabilities[1] > 0.8):
                    multiple_myeloma_counter = multiple_myeloma_counter + 1 

                patches_generated_count = patches_generated_count + 1
                if( patches_generated_count > 1000 ):
                    print("Analyzed 1000 patches")
                    print("Detected lung cancer in " + str(lung_cancer_counter) + " patches.")
                    print("Detected multiple myeloma in " + str(multiple_myeloma_counter) + " patches.")

                    exit(0)

slide.close() # Close the slide when done