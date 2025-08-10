# import YOLO model
from ultralytics import YOLO

# Load a model
model = YOLO('yolo11n-cls.pt') # load a pretrained model (recommended for training)

# Train the model
model.train(data='C:\Venky\cancer_ml_project\cancer_classification', epochs=50)