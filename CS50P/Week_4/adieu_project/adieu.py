# Import the inflect library
import inflect

# Initialize the inflect engine
p = inflect.engine()

# Create an empty list to store the names
names = []

print("Enter names one by one. Press Ctrl-D (or Ctrl-Z on Windows) when done.")

# Collect names until EOF
while True:
    try:
        # Continuously prompt the user for input
        name = input("Name: ")
        # Append each name to the list until the user signals EOF (Ctrl-D)
        names.append(name)
    except EOFError:
        break

# Remove duplicates while preserving order
names = list(dict.fromkeys(names))

"""
Check the length of the list:
- If there is only one name, format the output directly
- If there are two names, join them with "and"
- If there are three or more names, use commas and
  an Oxford comma before "and"
"""
if len(names) == 0:
    farewell = "No names were entered."
elif len(names) == 1:
    farewell = f"Adieu, adieu, to {names[0]}"
elif len(names) == 2:
    farewell = f"Adieu, adieu, to {names[0]} and {names[1]}"
else:
    farewell = f"Adieu, adieu, to {p.join(names)}"

# Print the final farewell message
if farewell:
    print(f"\n{farewell}")
