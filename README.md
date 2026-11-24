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
pip install monai torch matplotlib

## Image Source and Attribution
- **Image Source:** Nevit Dilmen, *Color Brain MRI 0284 15.jpg*, Wikimedia Commons, 2012.
- **License:** Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0).
- **Source URL:** [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Color_Brain_MRI_0284_15.jpg)
- **Image Description:** Trichromatic false-color brain MRI combining T1 (Red), PD (Green), and T2 (Blue) imaging channels.
- **Processing:** Image preprocessing and augmentation using Python, PyTorch, and MONAI.
