# Step 1: Define the menu as a dictionary
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0.00  # Step 2: Initialize total cost

# Step 3: Loop to continuously prompt the user
while True:
    try:
        # Step 4: Prompt user for item and convert input to title case
        item = input("Item: ").title()

        # Step 5: Check if item exists in the menu
        if item in menu:
            # Add the price of the item to the total if item in menu
            total += menu[item]

            # Step 6: Display the updated total formatted to two decimal places
            print(f"Total: ${total:.2f}")
    except EOFError:
        # Step 7: Break the loop when Control-D is pressed
        print()  # Print a newline for clean exit
        break