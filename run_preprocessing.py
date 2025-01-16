import os
import numpy as np
import pandas as pd
import SimpleITK as sitk
from preprocessing import normalize_hu, create_nodule_mask

# Paths
data_dir = "data/"
output_dir = "processed_data/"
annotations_file = "annotations/annotations.csv"

# Create output directories
os.makedirs(output_dir, exist_ok=True)

# Load annotations
annotations = pd.read_csv(annotations_file)
# Clean up leading or trailing spaces in the seriesuid column
annotations['seriesuid'] = annotations['seriesuid'].str.strip()


# Process each subset
for subset in range(10):
    subset_dir = os.path.join(data_dir, f"subset{subset}")
    output_subset_dir = os.path.join(output_dir, f"subset{subset}")
    os.makedirs(output_subset_dir, exist_ok=True)

    for filename in os.listdir(subset_dir):
        if filename.endswith(".mhd"):
            file_path = os.path.join(subset_dir, filename)

            # Extract the full series UID from the filename (without extension)
            series_uid = os.path.splitext(filename)[0]  # Remove ".mhd" extension

            print(f"Processing file: {filename}, Extracted series UID: {series_uid}")  # Debug

            # Load CT scan
            image = sitk.ReadImage(file_path)
            image_array = sitk.GetArrayFromImage(image)

            # Get origin and spacing from the CT metadata
            origin = np.array(image.GetOrigin())
            spacing = np.array(image.GetSpacing())[::-1]  # Reverse to match array shape (Z, Y, X)

            # Normalize HU values
            normalized_image = normalize_hu(image_array)

            # Create nodule mask
            nodule_mask = create_nodule_mask(normalized_image.shape, annotations, series_uid, origin, spacing)

            # Save preprocessed image and mask
            np.save(os.path.join(output_subset_dir, f"{series_uid}_image.npy"), normalized_image)
            np.save(os.path.join(output_subset_dir, f"{series_uid}_mask.npy"), nodule_mask)

            print(f"Processed {filename}")


