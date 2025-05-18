# filepath: d:\showcase_pictures\creativity\images\Mine_t\thumb_converter.py

from PIL import Image
import os

# Define the folder containing the thumbnails
input_folder = "d:/PROJECTS_STCEJORP/showcase_pictures/creativity_2/photography/images/fulls"
output_folder = "d:/PROJECTS_STCEJORP/showcase_pictures/creativity_2/photography/images/thumbs"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define the maximum size for thumbnails (e.g., 512x512)
max_size = (512, 512)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image
        with Image.open(input_path) as img:
            # Resize the image while maintaining aspect ratio
            img.thumbnail(max_size)

            # Save the compressed image
            img.save(output_path, optimize=True, quality=85)  # Adjust quality as needed (85 is a good balance)

        print(f"Compressed and resized: {filename}")

print("All thumbnails have been resized and compressed!")