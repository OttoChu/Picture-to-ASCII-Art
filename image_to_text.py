from PIL import Image
import os

def resize_image(image, max_side_length):
    """
    Resize the image while maintaining the aspect ratio.

    :param image: The input image.
    :type image: PIL.Image.Image
    :param max_side_length: The maximum length of the longest side.
    :type max_side_length: int
    :return: The resized image.
    :rtype: PIL.Image.Image
    """
    width, height = image.size
    if width > height:
        new_width = max_side_length
        new_height = int(height * (max_side_length / width))
    else:
        new_height = max_side_length
        new_width = int(width * (max_side_length / height))
    return image.resize((new_width, new_height))

def add_padding(image, original_size):
    """
    Add vertical padding to match the original aspect ratio.

    :param image: The input image.
    :type image: PIL.Image.Image
    :param original_size: The original size of the image.
    :type original_size: tuple
    :return: The padded image.
    :rtype: PIL.Image.Image
    """
    width, height = image.size
    new_image = Image.new("RGB", original_size)
    vertical_padding = (original_size[1] - height) // 2
    new_image.paste(image, ((original_size[0] - width) // 2, vertical_padding))
    return new_image

# Get a list of all image files in the current directory
image_files = [file for file in os.listdir() if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Define the maximum side length
max_side_length = 575

# Resize each image
for input_file in image_files:
    # Open the image
    image = Image.open(input_file)

    # Resize the image while maintaining aspect ratio
    resized_image = resize_image(image, max_side_length)

    # Add padding to match the original aspect ratio
    padded_image = add_padding(resized_image, image.size)

    # Save the resized and padded image with the same file name
    padded_image.save(input_file)