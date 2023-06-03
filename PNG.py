from PIL import Image

input_image_path = "spider.png"
output_image_path = "spider_compressed1.png"

with Image.open(input_image_path) as input_image:
    # Save the image in PNG format with compression level 9 (maximum compression)
    input_image.save(output_image_path, format='PNG', compress_level=5)

