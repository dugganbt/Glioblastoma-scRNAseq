"""
Accession numbers

GSE214966 (scRNA-seq for four patients at baseline):
This will allow you to perform clustering and identify cellular heterogeneity in glioblastoma at baseline.

GSE214967 (scRNA-seq for vortioxetine vs. DMSO): 
You can analyze how treatment with vortioxetine affects different cell populations compared to the control (DMSO),
which will directly relate to drug effects.
"""

# DATA IMPORT
import GEOparse

baseline_accession_number = "GSE214966"
treated_accession_number = "GSE214967"

# Downloading the data from GEO
# gse = GEOparse.get_GEO(geo=baseline_accession_number, destdir="./")
# gse = GEOparse.get_GEO(geo=treated_accession_number, destdir="./")

# Once downloaded, import locally instead
baseline_path = f"./{baseline_accession_number}_family.soft.gz"
# treated_path = f"./{treated_accession_number}_family.soft.gz"

# Load the GEO dataset from the local file
gse_baseline = GEOparse.get_GEO(filepath=baseline_path)

# Check the dataset info to verify it loaded correctly
print(gse_baseline)


# DATA EXPLORATION
import pandas as pd

# List available data tables
print(gse_baseline.gsms)  # List of all samples
print(gse_baseline.gpls)  # List of platform information
