from PIL import Image
import os

ASCII_CHARS = '@%#*+=-:. '

def resize_image(image, max_side_length):
    # Resize the image while maintaining the aspect ratio
    width, height = image.size
    max_dimension = max(width, height)
    if max_dimension > max_side_length:
        scale_factor = max_side_length / max_dimension
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        return image.resize((new_width, new_height))
    return image

def convert_image_to_ascii(image):
    # Convert the image to ASCII art
    width, height = image.size
    aspect_ratio = 2.0
    ascii_pixels = []
    max_y = height - 1 if height % 2 == 0 else height - 2
    for y in range(0, max_y, 2):
        ascii_row = []
        for x in range(width):
            pixel_upper = image.getpixel((x, y))
            pixel_lower = image.getpixel((x, y + 1))
            brightness_upper = sum(pixel_upper) // 3
            brightness_lower = sum(pixel_lower) // 3
            char_index_upper = min(int(brightness_upper / 256 * len(ASCII_CHARS)), len(ASCII_CHARS) - 1)
            char_index_lower = min(int(brightness_lower / 256 * len(ASCII_CHARS)), len(ASCII_CHARS) - 1)
            ascii_char_upper = ASCII_CHARS[char_index_upper]
            ascii_char_lower = ASCII_CHARS[char_index_lower]
            ascii_row.append(ascii_char_upper)
            ascii_row.append(ascii_char_lower)
        ascii_pixels.append(''.join(ascii_row))
    if height % 2 != 0:
        # Handle the last row separately if the height is odd
        last_row = []
        for x in range(width):
            pixel = image.getpixel((x, height - 1))
            brightness = sum(pixel) // 3
            char_index = min(int(brightness / 256 * len(ASCII_CHARS)), len(ASCII_CHARS) - 1)
            ascii_char = ASCII_CHARS[char_index]
            last_row.append(ascii_char)
        ascii_pixels.append(''.join(last_row))
    return '\n'.join(ascii_pixels)

# Get a list of all image files in the current directory
image_files = [file for file in os.listdir() if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Define the maximum side length
max_side_length = 575

# Process each image
for input_file in image_files:
    # Open the image
    image = Image.open(input_file)

    # Resize the image while maintaining aspect ratio
    resized_image = resize_image(image, max_side_length)

    # Convert the image to ASCII art
    ascii_art = convert_image_to_ascii(resized_image)

    # Generate the output file name
    output_file = os.path.splitext(input_file)[0] + ".txt"

    # Save the ASCII art to the output file
    with open(output_file, "w") as file:
        file.write(ascii_art)

    print(f"Generated {output_file}")