# Import necessary modules
#   - sys: to access command-line arguments and exit the program
import sys
import csv
from tabulate import tabulate

# Step 1: Ensure exactly one command-line argument is passed
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Step 2: Get the filename from command-line arguments
filename = sys.argv[1]

# Step 3: Ensure the file is a CSV
if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    # Step 4: Open and read the CSV file
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader) # Convert iterator to a list

        # Step 5: Check if the CSV file is empty
        if not data:
            sys.exit("CSV file is empty")

        # Step 6: Print the formatted table
        print(tabulate(data, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
