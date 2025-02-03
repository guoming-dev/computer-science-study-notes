# Step 1: Get user input
text = input("Type something: ")

# Step 2: Replace text faces with emojis
text = text.replace(":)", "🙂")
text = text.replace(":(", "🙁")

# Step 3: Display the modified text
print(text)