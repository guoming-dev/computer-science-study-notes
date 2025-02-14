# Import Random
import random


def get_level():
    """
    1. Prompt the user for a level (n)
        - Keep prompting the user until they enter a valid level (1, 2, or 3).
        - Ensure input is an integer; if not, catch errors and reprompt.
    """
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n    # Return the valid input
            else:
                # Give feedback
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            # Handle non-integer inputs
            print("Invalid input. Please enter a number.")


def generate_integer(level):
    """
    2. Generate a random integer based on the level
        - If level == 1 → Generate numbers from 0 to 9.
        - If level == 2 → Generate numbers from 10 to 99.
        - If level == 3 → Generate numbers from 100 to 999.
    """

    for _ in range(10):  # Generate 10 random numbers
        match level:
            case 1:
                # Generate random integers from 0 to 9.
                return random.randint(0,9)
            case 2:
                # Generate random integers from 10 to 99.
                return random.randint(10, 99)
            case 3:
                # Generate random integers from 100 to 999.
                return random.randint(100, 999)

def main():
    """
    3. Run the quiz logic
        - Initialize a score counter at 0.
        - Repeat for 10 random math problems:
            - Generate two numbers using the generate_integer function.
            - Prompt the user for the sum (X + Y).
            - Allow up to 3 attempts to answer correctly:
                - If the user answers correctly, increase the score and move to the next question
                - If incorrect, print "EEE" and allow another attempt.
                - If all 3 attempts fail, display the correct answer.
    """
    # Step 1: Get level from user
    level = get_level()

    # Step 2: Initialize score counter
    score = 0

    # Step 3: Loop 10 times to generate and ask questions
    for _ in range(10):
        # Generate two numbers based on the level
        x = generate_integer(level)    # Fetch first operand
        y = generate_integer(level)    # Fetch second operand
        correct_answer = x + y  # Compute correct sum

        # Step 4: Allow up to 3 attempts
        for attempt in range(3):
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    score += 1  # Increase score if correct answer
                    break   # Move to the next question
                else:
                    print("EEE")    # Print error message for wrong answer
            except ValueError:
                print("EEE")    # Print error for non-integer input

        # Step 5: If user failed 3 attempts, show correct answer
        else:
            print(f"{x} + {y} = {correct_answer}")

    # 4. Display the final score out of 10.
    print(f"Score: {score}")

if __name__ == "__main__":
    main()
