from PIL import Image
import os

def resize_and_compress_images(input_folder, output_folder, target_size_kb, new_width=None, new_height=None, resolution=None):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get a list of all files in the input folder
    files = os.listdir(input_folder)
    
    # Loop through each file in the input folder
    for file_name in files:
        # Check if the file is an image
        if file_name.endswith(('.jpg', '.jpeg','webp' ,'.png', '.bmp')):
            # Open the image file
            input_image_path = os.path.join(input_folder, file_name)
            output_image_path = os.path.join(output_folder, file_name)
            with Image.open(input_image_path) as image:
                # Resize the image if new width and height are specified
                if new_width and new_height:
                    image = image.resize((new_width, new_height))
                
                # Change the resolution if specified
                if resolution:
                    dpi_width, dpi_height = resolution
                    image.info['dpi'] = (dpi_width, dpi_height)
                
                # Set initial quality
                quality = 60
                
                # Loop to find the optimal quality to achieve the target size
                while True:
                    # Save the image with the current quality
                    image.save(output_image_path, quality=quality)
                    
                    # Check the size of the saved image
                    size_kb = os.path.getsize(output_image_path) / 1024
                    
                    # If the size is within the target range, break the loop
                    if size_kb <= target_size_kb:
                        break
                    
                    # Reduce the quality for the next iteration
                    quality -= 5
                    if quality < 5:
                        # If quality is very low and still not meeting target size, break the loop
                        break

input_folder = 'input_images'
output_folder = 'compressed_images'
target_size_kb = 8  # Target size in kilobytes
new_width = 400
new_height = 400
resolution = (300, 300)  # Resolution in DPI (dots per inch)

resize_and_compress_images(input_folder, output_folder, target_size_kb, new_width, new_height, resolution)
