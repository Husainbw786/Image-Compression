

# Image Compression Tool


The Image Compression Tool is a Python mini-project that allows you to compress JPEG and PNG image files. It provides a user-friendly interface to select an input image, specify the desired width for the resized image, and save the compressed output image with the appropriate format.

## Features

- **File Selection**: The tool utilizes the Tkinter library to display a file dialog, enabling users to select an input image file and choose the location to save the compressed output image.

- **Image Compression**: The selected image file is opened using the PIL (Pillow) library, resized according to the desired width specified by the user, and compressed to reduce the file size while maintaining visual quality.

- **Supported Formats**: The tool supports both JPEG (.jpg, .jpeg) and PNG (.png) image formats. The output image is saved with the corresponding file extension based on the input file type.

- **Optimization**: The resized image is optimized during the compression process, ensuring efficient file storage and fast loading times.

## Usage

1. Run the Python script `image_compression.py`.

2. The tool will display a file dialog for you to select the input image file (.jpg, .jpeg, .png).

3. After selecting the input file, another file dialog will appear for you to specify the location and filename to save the compressed output image.

4. Enter the desired width for the resized image in pixels. The tool will automatically calculate the corresponding height to maintain the aspect ratio.

5. Click the "Save" or "OK" button in the file dialog to initiate the compression process.

6. The tool will resize and compress the image based on your input, and save the output image with the appropriate format.

7. The compressed image will be available at the specified location.

## Requirements

- Python 3.x
- Tkinter library
- PIL (Pillow) library

## Installation

1. Clone the repository or download the project files.

2. Install the required dependencies using the following command:

   ```
   pip install tkinter pillow
   ```

3. Run the Python script `image_compression.py` to launch the Image Compression Tool.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Image Compression Tool is based on the Python programming language and utilizes the Tkinter and PIL (Pillow) libraries.
- Special thanks to the developers and contributors of the open-source tools used in this project.

Feel free to customize and enhance the README file based on your specific project details, such as adding screenshots, installation instructions, or any additional features or functionalities that are not mentioned in the provided code.
