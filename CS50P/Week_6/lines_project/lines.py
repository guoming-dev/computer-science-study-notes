# Import necessary modules
#   - sys: to access command-line arguments and exit the program
#   - os: to check if the file exists
import sys
from pathlib import Path

# Define the main function
# - This function will handle command-line arguments and file validation
#    - Check the number of command-line arguments
def main():
#   - If less than 2 arguments (only the script name provided),
#     exit with "Too few command-line arguments"
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
#   - If more than 2 arguments (script name + more than one file),
#     exit with "Too many command-line arguments"
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
#       - Store the filename from command-line arguments

    filename = sys.argv[1]
    extension = Path(filename).suffix
#   Validate if the file has a '.py' extension
#   - If not, exit with "Not a Python file"
    if extension != '.py':
            sys.exit("Not a Python file")

#   Try to count valid lines in the file
    try:
        valid_lines = count_lines(filename)
#       Print the total count of valid lines
        print(valid_lines)

    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

# Define a helper function to count valid lines of code in the file
#   - This function will read the file line by line and count only the lines of code
def count_lines(filename):
#   - Initialize a counter to keep track of valid lines
    count = 0
#   - Open the file in read mode
    with open(filename, "r") as file:
#       - Iterate through each line in the file
        for line in file:
#           - Strip leading whitespace from the line
            stripped = line.strip()
#           - If the line is empty or contains only whitespace, skip it
#           - If the line starts with a '#' after stripping whitespace, skip it (comment line)
            if stripped == "" or stripped.startswith("#"):
                continue
#           - Otherwise, count the line as valid code
            count += 1
#   - Return the total count of valid lines
    return count

if __name__ == "__main__":
    main()
