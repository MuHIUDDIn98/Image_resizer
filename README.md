# Image Resize and Compression Script

This script resizes and compresses images in a specified input folder and saves the processed images to an output folder. It allows you to specify target size, dimensions, and resolution for the output images.

## Usage

1. **Import Required Libraries**

```python
from PIL import Image
import os
`````
#Set Parameters and Execute the Function
```
input_folder = 'input_images'
output_folder = 'compressed_images'
target_size_kb = 8  # Target size in kilobytes
new_width = 400
new_height = 400
resolution = (300, 300)  # Resolution in DPI (dots per inch)

resize_and_compress_images(input_folder, output_folder, target_size_kb, new_width, new_height, resolution)
```````
