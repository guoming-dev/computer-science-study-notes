import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

valid_extensions = [".jpg", ".jpeg", ".png"]

input_file = sys.argv[1]
output_file = sys.argv[2]

input_ext = os.path.splitext(input_file)[1].lower()
output_ext = os.path.splitext(output_file)[1].lower()

if input_ext not in valid_extensions or output_ext not in valid_extensions:
    sys.exit("Invalid input")
if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

if not os.path.isfile(input_file):
    sys.exit("Input does not exist")

try:
    # Open the input image and shirt image
    input_image = Image.open(input_file)
    # Make sure shirt.png is in the same directory
    shirt_image = Image.open("shirt.png")

    # Resize the input image to match the shirt image
    input_image = ImageOps.fit(input_image, shirt_image.size)

    # Overlay the shirt on the resized input image
    input_image.paste(shirt_image, (0, 0), shirt_image)

    # Save the final image
    input_image.save(output_file)

except Exception as e:
    sys.exit(f"An error occurred: {e}")
