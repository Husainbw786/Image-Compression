from tkinter import filedialog

from PIL import Image


input_image_path = 'nature.jpg'
output_image_path = 'nature_compressed1.jpg'

with Image.open(input_image_path) as input_image:
    # Save the image in JPEG format with a high quality setting (90)
    #  More the quality more less will be the compresion.
    input_image.save(output_image_path, format='JPEG', quality=10)
