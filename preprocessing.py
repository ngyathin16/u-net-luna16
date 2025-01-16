import numpy as np
import pandas as pd
import SimpleITK as sitk

def load_ct_scan(filepath):
    """
    Load a CT scan and return its array representation.
    """
    image = sitk.ReadImage(filepath)
    image_array = sitk.GetArrayFromImage(image)
    return image_array

def normalize_hu(image):
    """
    Normalize the Hounsfield Units (HU) of a CT scan to [0, 1].
    """
    image = np.clip(image, -1000, 400)  # Clip HU values to the specified range
    image = (image - (-1000)) / (400 - (-1000))  # Scale to [0, 1]
    return image

def create_nodule_mask(image_shape, annotations, series_uid, origin, spacing):
    """
    Create a binary mask with nodules marked as 1 based on the annotations.

    Args:
        image_shape (tuple): Shape of the CT scan (depth, height, width).
        annotations (pd.DataFrame): DataFrame containing nodule annotations.
        series_uid (str): Series UID for the current CT scan.
        origin (tuple): Origin of the CT scan in world coordinates.
        spacing (tuple): Voxel spacing (depth_spacing, height_spacing, width_spacing).

    Returns:
        np.ndarray: Binary mask with nodules marked as 1.
    """
    mask = np.zeros(image_shape, dtype=np.uint8)

    # Filter annotations for the current series UID
    nodules = annotations[annotations['seriesuid'] == series_uid]

    print(f"Processing series UID: {series_uid}")
    print(f"Origin: {origin}, Spacing: {spacing}, Image Shape: {image_shape}")

    if nodules.empty:
        print(f"Skipping {series_uid}: No annotations found.")
        return mask

    if nodules.empty:
        print(f"No annotations found for series UID: {series_uid}")
        return mask

    for _, row in nodules.iterrows():
        print(f"Processing annotation: {row}")

        # Convert nodule center from world coordinates to voxel coordinates
        center = np.array([
            (row['coordZ'] - origin[0]) / spacing[0],  # Convert Z
            (row['coordY'] - origin[1]) / spacing[1],  # Convert Y
            (row['coordX'] - origin[2]) / spacing[2],  # Convert X
        ])
        radius = row['diameter_mm'] / 2 / spacing[0]  # Convert radius to voxel space

        print(f"Converted center (voxel): {center}, Radius (voxel): {radius}")

        # Clamp center to within bounds
        center = np.clip(center, [0, 0, 0], [image_shape[0] - 1, image_shape[1] - 1, image_shape[2] - 1])
        print(f"Clamped center (voxel): {center}")

        # Compute voxel coordinates
        z, y, x = np.ogrid[:image_shape[0], :image_shape[1], :image_shape[2]]
        distance = np.sqrt((z - center[0]) ** 2 + (y - center[1]) ** 2 + (x - center[2]) ** 2)

        # Add the sphere to the mask
        mask[distance <= radius] = 1

        print(f"Mask updated: Unique values: {np.unique(mask)}")

    print(f"Final mask shape: {mask.shape}, Unique values: {np.unique(mask)}")
    return mask


