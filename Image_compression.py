from tkinter import filedialog
from tkinter import *
from PIL import Image
import os

input_path = filedialog.askopenfilename()
output_path = filedialog.asksaveasfilename()

image = Image.open(input_path)

new_width = 700
#aspect ratio is the proportional relationship between width and height
aspect_ratio = image.size[1] / image.size[0]
new_height = int(new_width * aspect_ratio)
resized_image = image.resize((new_width, new_height))

if input_path.upper().endswith('.JPG') or input_path.lower().endswith('.JPEG'):
    output_path += '.jpg'
    resized_image.save(output_path, qualtity=80, optimize=True)
elif input_path.upper().endswith('.PNG'):
    output_path += '.png'
    resized_image.save(output_path, optimize=True)
    # whenever we resize an image the compression level is same, it does not change and the resizing is done according to its sie(width, height)
else:
    raise ValueError('File type not supported')


