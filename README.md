# Medical Image Preprocessing with MONAI

This project demonstrates a basic medical image preprocessing pipeline using the **MONAI** (Medical Open Network for AI) framework.

## Features
- Loads a medical image (MRI).
- Applies standard MONAI transformations:
  - Intensity scaling (normalization)
  - Resizing
  - Random 90-degree rotation (data augmentation)
- Handles RGB, Grayscale, and RGBA images.
- Visualizes the processed image using Matplotlib.

## Prerequisites
- Python 3.x
- MONAI
- PyTorch
- Matplotlib

## Installation
```bash
pip install monai torch matplotlib