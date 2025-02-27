# Import necessary modules
#   - sys: to access command-line arguments and exit the program
#   - csv: to read and write tabular data in CSV format.
import sys
import csv

def main():
    # Ensure correct number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Input file comes before output file
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # Read the input CSV file
        with open(input_file, newline='') as file:
            reader = csv.DictReader(file)

            # Prepare the output file
            with open(output_file, "w", newline='') as new_file:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                writer.writeheader()

                # Process each row
                for row in reader:
                    last, first = row["name"].split(", ")   # Split "Last, First"
                    writer.writerow({"first": first, "last": last, "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
