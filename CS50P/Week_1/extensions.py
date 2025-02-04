import sys  # Importing sys to use sys.exit()

# Step 1: Get name of the file
# - Prompt the user for input
file_name = input("File name: ")

# Step 2: Validate user's input
# - If file name is empty, print "Invalid file name!" and exit
if not file_name.strip():
    print("Invalid file name!")
    sys.exit()

# Step 3: Normalize the file name
# - Convert the file name to lowercase
file_name = file_name.strip().lower()

# Step 4: Validate the extension
# - Check if the file name contains a '.'
# - If there is no '.' or the '.' is at the start of the file name, print "application/octet-stream" and exit
def check_extension(normalized_filename):
    if '.' not in normalized_filename or normalized_filename.startswith("."):
        print("application/octet-stream")
        sys.exit() # Exit the program as no valid extension exists

# Step 5: Extract and check the file extension
# - Extract the substring after the last '.' (suffix)
extension = file_name.rsplit(".", 1)[-1] # Get the part after the last '.'

# - Use a dictionary to map extensions to media types:
media_types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

# Step 6: Determine and output the media type
# - If the suffix exists in the dictionary, print the corresponding media type
if extension in media_types:
    print(media_types[extension])
# - If the suffix doesn't exist, print "application/octet-stream"
else:
    print("application/octet-stream")