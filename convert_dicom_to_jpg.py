import dicom2jpg

def main():
    export_location = "C:/Venky/cancer_ml_project/dicom_to_jpg/"

    # Or convert all DICOM files in a directory
    dicom_dir = "C:/Venky/cancer_ml_project/manifest-1746712105220/CMB-MML/MSB-00089/11-05-1959-NA-CTAbdPelvis-57955/3.000000-NA-35008"
    dicom2jpg.dicom2jpg(dicom_dir, target_root=export_location)

if __name__ == '__main__':
    main()

