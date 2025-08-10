## Cancer detection in whole slide images.

* The idea of this project is to download whole slide images (in svs format) from the TCIA website. Using these massive whole slide images, generate patches that are of 255x255 and then save them into a test/train folder. Using yolov11 train a custom image classification module that can detect what type of cancer could be there in a whole slide image by looking at sections of the wsi, and applying the classification model on top of that extracted patch.

### Steps
* Download the following whole side images. Since they are very massive we get 2-3 images per type. 2 for lung cancer, and 2 for multiple myeloma.

https://www.cancerimagingarchive.net/collection/cmb-mml/

https://www.cancerimagingarchive.net/collection/cmb-lca/

Download the SVS format files. A new web page opens and we can pick 1-2 svs files for download. We will need to install a browser extension to allow these to download in the background. Once they are done, we can store them in a folder called svsimages.

* We now need to extract patches from this svs image. We are using the openslide python library to do this. It allows us to read sections of the image giving a specific point and width and length to create a patch. We will need to convert the extracted image to RGB format to store as JPG. Without doing this we are not able to train these images in Yolov11 because the size of the patch images are too large for the ML model to handle.

* Once the patches are created, we need to put them into a directory structure to allow us to train the YoloV11 image classification model. We create a root level directory.

ROOT
    train
        CMB-LCA
            800+ jpg images (patches extracted from wsi)
        CMB_MML
            800+ jpg images (patches extracted from wsi)
    test
        CMB-LCA
            125+ jpg images (patches extracted from wsi)
        CMB_MML
            125+ jpg images (patches extracted from wsi)

* Once the directory is in place with the images we can train the model. We have trained it for 50 epochs.

* Once the model is present, we now can use a new WSI image and run the detection. The detection module also splices the images into small 225x225 patches, converts them to JPG after checking that the patch is not entirely background, and applies the ML model. 

* If we run the detection on the same WSI images we had used to train, the accuracy is almost 100% as expected. With a new WSI, the accuracy rates are pretty much 50/50. This means that the model is not good and need to be fed a lot more images from a variety of WSIs and made more accurate.