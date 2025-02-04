# Import necessary libraries
import sys
import pyfiglet
import random

# Check command-line arguments
if len(sys.argv) not in [1, 3]:
    # Exit if arguments are invalid
    sys.exit("Usage: figlet.py [-f or --font FONTNAME]")

# If two arguments are provided
if len(sys.argv) == 3:
    # Validate the first argument
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid argument. Use -f or --font.")
    # Validate the font name
    font_name = sys.argv[2]
    try:
        pyfiglet.FigletFont.getFonts().index(font_name)
    except ValueError:
        sys.exit("Invalid font name.")

# If no arguments are provided, select a random font
else:
    font_name = random.choice(pyfiglet.FigletFont.getFonts())

# Prompt the user for text input
text = input("Input text: ")

# Generate ASCII art
figlet = pyfiglet.Figlet(font=font_name)
ascii_art = figlet.renderText(text)

# Output the ASCII art
print(ascii_art)
