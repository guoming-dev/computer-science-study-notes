# Step 1: Define a dictionary with fruits and their calorie counts
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

# Step 2: Prompt the user for input and normalize using .lower()
user_fruit = input("Item: ").lower()

# Step 3: Check if the fruit exists in the dictionary
if user_fruit in fruits:
    # Step 4: Display the Calories if fruit exists in dictionary
    print("Calories", fruits[user_fruit], sep=": ")
else:
    # Step 5: If no match is found, do nothing
    pass