import pydicom
import numpy as np
import matplotlib.pyplot as plt

# Specify the path to your DICOM file
dicom_file_path = "C:/Venky/cancer_ml_project/manifest-1746712105220/CMB-MML/MSB-00089/11-05-1959-NA-CTAbdPelvis-57955/1.000000-Scout-46111/1-1.dcm"
# Read the DICOM file
dataset = pydicom.dcmread(dicom_file_path)
print('------------------------------------------')
print(dataset)
print('------------------------------------------')
patient_name = dataset.PatientName
patient_id = dataset.PatientID
study_date = dataset.StudyDate

# Accessing metadata by tag (hexadecimal representation)
# For example, PatientName has tag (0010, 0010)
patient_name_by_tag = dataset[0x0010, 0x0010].value

print(f"Patient Name: {patient_name}")
print(f"Patient ID: {patient_id}")
print(f"Study Date: {study_date}")

# Access the pixel array
pixel_array = dataset.pixel_array

plt.imshow(pixel_array, cmap='gray')
plt.show()