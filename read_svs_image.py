import slideio
import matplotlib.pyplot as plt

image_path='C:\Venky\cancer_ml_project\svs_images\MSB-00089-02-16.svs'
slide = slideio.open_slide(image_path,'SVS')
num_scenes = slide.num_scenes
scene = slide.get_scene(0)
print(num_scenes, scene.name, scene.rect, scene.num_channels)

raw_string = slide.raw_metadata
raw_string = raw_string.split("|")
print(raw_string)

# Get the first scene.
scene  = slide.get_scene(0)
print('Scene Name ' + str(scene.name))
print('Scene rect ' + str(scene.rect))
print('Scene num_channels ' + str(scene.num_channels))
print('Scene resolution ' + str(scene.resolution))

# Read a small section of the image
image = scene.read_block(size=(500,0))

plt.imshow(image)
plt.show()

# Read a large section of the image and shrink it
image = scene.read_block((5000, 5000, 5000, 5000), size=(500,0))
plt.imshow(image)
plt.show()

# Read just the first channel.
image = scene.read_block((5000, 5000, 5000, 5000), size=(500,0), channel_indices=[0])
plt.imshow(image, cmap='gray')
plt.show()