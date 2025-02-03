# Step 1: Prompt the user for the bill amount and strip the $ symbol
bill_input = input("Enter the bill amount: ")
# Remove the $ symbol and convert to float
bill = float(bill_input.replace("$", ""))

# Step 2: Prompt the user for the tip percentage and strip the % symbol
tip_input = input("Enter the tip percentage: ")
# Remove the % symbol and convert to float
tip_percentage = float(tip_input.replace("%", ""))

# Step 3: Calculate the tip amount
tip = bill * (tip_percentage / 100)

# Step 4: Ensure exact output format
print(f"Leave ${tip:.2f}")