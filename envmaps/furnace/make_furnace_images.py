#!/usr/bin/env python3

from PIL import Image

# Image dimensions
width, height = 100, 50

# Grayscale value (0.8 out of 1) converted to 8-bit grayscale (0-255)
gray_value = int(0.8 * 255)

# Create an image with the given grayscale color
image = Image.new('L', (width, height), gray_value)

# Save the image as PNG
image.save('latlon_furnace_0_8_100x50.png')

