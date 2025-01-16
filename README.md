# U-Net Implementation for Lung Nodule Segmentation Using the LUNA16 Dataset

This project implements a 3D U-Net model for lung nodule segmentation using the LUNA16 dataset. It includes preprocessing, data augmentation, model training, and evaluation steps to accurately identify nodules in 3D CT scans. The aim is to provide a robust deep learning-based approach for medical image segmentation.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset Description](#dataset-description)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Results](#results)
7. [Acknowledgments](#acknowledgments)
8. [License](#license)

---

## Project Overview

Lung cancer is one of the leading causes of cancer-related deaths worldwide. Accurate identification and segmentation of lung nodules in CT scans is critical for early diagnosis and treatment planning. This project leverages the 3D U-Net architecture to segment lung nodules from the LUNA16 dataset, a popular benchmark for pulmonary nodule detection.

---

## Dataset Description

The [LUNA16 dataset](https://luna16.grand-challenge.org/) contains 3D CT scans of the lungs and corresponding nodule annotations. It provides:
- CT scan `.mhd` files with associated voxel information.
- Nodule annotations including location (x, y, z) and diameter in millimeters.

Preprocessing steps include:
1. Normalizing Hounsfield Unit (HU) values.
2. Converting nodule annotations from world coordinates to voxel coordinates.
3. Generating 3D binary masks with nodules marked as `1`.

---

## Project Structure

U-net-paper/
├── annotations/
│ ├── annotations.csv # Nodule annotation file
├── data/
│ ├── masks/ # Directory for preprocessed masks
│ ├── processed_data/ # Preprocessed CT scans and masks
│ ├── raw/ # Original LUNA16 CT scans
├── scripts/
│ ├── augmentations/ # Data augmentation scripts
│ ├── dataset/ # Dataset loading and preprocessing
│ ├── unet_model.py # U-Net 3D implementation
│ ├── train_unet.py # Training script
│ ├── evaluationScript/ # Evaluation metrics (e.g., Dice Coefficient)
├── venv/ # Virtual environment (optional)
├── requirements.txt # Required Python packages
├── README.md # Project documentation
# U-Net for LUNA16

This repository contains a 3D U-Net implementation for the LUNA16 dataset, aimed at biomedical image segmentation.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ngyathin16/u-net-luna16.git
   cd u-net-luna16
   ```
2. **Set up a virtual environment (optional)**
  ```bash
  python -m venv venv
  source venv/bin/activate        # On Windows: venv\Scripts\activate
  ```
3. **Install dependencies**
  ```bash
   pip install -r requirements.txt
  ```
4. **Download the dataset**
   Download the LUNA16 dataset from the official site.
   Place the .mhd files in the data/raw/ directory.
   Place the annotations.csv file in the annotations/ directory.

## Usage
1. **Preprocess the data**
   ```bash
   python run_preprocessing.py
   ```
2. **Train the U-net model**
   ```bash
   python train_unet.py
   ```
3. **Evaluate the model**
   ```bash
   python scripts/evaluationScript/evaluate.py
   ```

## Results

### Metrics
| Metric              | Value  |
|---------------------|--------|
| Dice Coefficient    | 87.65% |
| IoU                 | 79.34% |

## Acknowledgments

- **LUNA16 Dataset**: Dataset provided by the [LUNA16 Challenge](https://luna16.grand-challenge.org/).
- **U-Net Architecture**: Inspired by "[U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597)" by Olaf Ronneberger et al.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

   




