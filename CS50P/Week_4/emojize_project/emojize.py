import importlib.util

# Check if the emoji library is installed
if importlib.util.find_spec("emoji") is not None:
    import emoji

    # Prompt the user for input
    user_input = input("Input: ")

    # Convert emoji shortcodes to actual emojis
    converted_text = emoji.emojize(user_input, language='alias')

    # Display the converted text
    print(f"Output: {converted_text}")

else:
    print(
        "The 'emoji' library is not installed. " 
        "Please install it using 'pip install emoji'.")