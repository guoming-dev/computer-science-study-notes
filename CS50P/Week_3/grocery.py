# Initialize an empty dictionary to store items and their counts
grocery_list = {}

# Use a loop to continuously prompt the user for input
while True:
    try:
        # Get user input and convert to lowercase
        item = input().strip().lower()
        # Add item to dictionary or increment its count  
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    # Break loop when user ends input with Control-D
    except EOFError:
        break  

# Sort dictionary alphabetically and format output
for item in sorted(grocery_list):
    print(f"{grocery_list[item]} {item.upper()}")