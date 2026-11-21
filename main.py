
import torch
from monai.transforms import (
    Compose, ScaleIntensity, Resize, RandRotate90
)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# 1. Define MONAI transformation pipeline
transforms = Compose([
    ScaleIntensity(),
    Resize((256, 256)),
    RandRotate90(prob=1.0, spatial_axes=(0, 1))
])

# 2. Define image path
image_path = "Data/sample.jpg"

if not os.path.exists(image_path):
    print("Error: Image not found! Ensure sample.jpg is inside Data folder.")
else:
    # 3. Load image
    img_array = mpimg.imread(image_path)
    img_tensor = torch.tensor(img_array).float()

    # Handle grayscale, RGB, or RGBA images
    if img_tensor.ndim == 2:
        img_tensor = img_tensor.unsqueeze(0)  # H,W -> 1,H,W

    elif img_tensor.ndim == 3:
        if img_tensor.shape[-1] == 4:
            img_tensor = img_tensor[..., :3]  # Remove alpha channel

        img_tensor = img_tensor.permute(2, 0, 1)  # H,W,C -> C,H,W

    # 4. Apply MONAI transformations
    try:
        transformed_image = transforms(img_tensor)

        print("Success! Image processed successfully.")
        print(f"Shape: {transformed_image.shape}")

        # 5. Display processed image
        plt.figure(figsize=(6, 6))

        if transformed_image.shape[0] == 3:
            display_img = transformed_image.permute(1, 2, 0).numpy()
            plt.imshow(display_img)
        else:
            plt.imshow(transformed_image[0].numpy(), cmap="gray")

        plt.title("Processed MRI with MONAI")
        plt.axis("off")
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")
