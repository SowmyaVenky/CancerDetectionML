## Look at the code in this notebook for reference.
## https://github.com/kirbyju/TCIA_Notebooks/blob/main/TCIA_Segmentations.ipynb

from tcia_utils import nbia

df = nbia.getSeries(collection = "CMB-MML", format = "df")
sorted = df.sort_values(["PatientID", "SeriesDescription"])
print(sorted.head(4))

df1 = nbia.getSeries(collection = "CMB-MML", modality = "RTSTRUCT", format = "df")
print(df1)