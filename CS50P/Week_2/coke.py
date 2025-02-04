"""
Step 1: Set the price of a Coke to 50¢
"""
PRICE = 50

"""
Step 2: Initialize the amount due to 50¢
"""
amount_due = PRICE

"""
Step 3: While the amount due is greater than 0:
    a. Display the current amount due
    b. Prompt the user to insert a coin
    c. If the coin is valid (25¢, 10¢, 5¢):
        i. Deduct the coin value from the amount due
    d. If the coin is invalid:
        i. Silently ignore the input and loop back to prompt again
"""
while amount_due > 0:
    print(f"Amount Due: {amount_due}")  # Display the current amount due
    coin = int(input("Insert Coin: "))  # Prompt the user to insert a coin
    # Only process valid coins
    if coin in [5, 10, 25]:
        amount_due -= coin  # Deduct the coin value
        # Invalid coins are ignored; no message is printed

"""
Step 4: After exiting the loop:
    a. If the amount due is exactly 0:
        i. Print "Change Owed: 0"
    b. If the amount due is less than 0:
        i. Calculate and display the change owed
"""
if amount_due == 0:
    print("Change Owed: 0")  # Exact payment
else:
    print(f"Change Owed: {abs(amount_due)}")  # Display the change owed