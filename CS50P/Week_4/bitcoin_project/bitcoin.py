# Import necessary libraries
import requests
import sys
"""
Prompt the user for a valid Bitcoin quantity (n)
    - Keep prompting the user until they enter a valid input:
        - Input should be a positive number (greater tan zero).
        - Input should not contain letters, special characters, or negative values.
"""
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoin_amount = float(sys.argv[1])
    if bitcoin_amount <= 0:
        sys.exit("Bitcoin amount must be a positive number")
except ValueError:
    sys.exit("Command-line argument is not a number")

"""
Fetch the current price of Bitcoin from the CoinCap API:
    - API URL: https://api.coincap.io/v2/assets/bitcoin
    - Extract the current Bitcoin price from the JSON response.
    - Handle network errors (e.g., no internet connection or API failure).
"""
API_URL = "https://api.coincap.io/v2/assets/bitcoin"

try:
    response = requests.get(API_URL)
    response.raise_for_status() # Raises an error for bad responses (4xx, 5xx)
    data = response.json()  # Convert API response to Python dictionary
    bitcoin_price = float(data["data"]["priceUsd"]) # Extract price from JSON
except requests.RequestException:
    sys.exit("Error fetching Bitcoin price")

"""
Calculate the total cost:
    - Multiply the user's Bitcoin quantity (n) by the current price of Bitcoin.
"""
total_price = bitcoin_amount * bitcoin_price

"""
Format and display the correct output:
    - Ensure the total cost is rounded to four decimal places.
    - Use commas as thousands separators for better readability.
"""
print(f"${total_price:,.4f}")