import random

# Function to roll a dice
def roll_dice(sides=6):
    return random.randint(1, sides)

# Main function
def main():
    while True:
        print("\nRolling the dice...")
        sides = input("Enter the number of sides for the dice (default is 6) or 'q' to quit: ")
        
        if sides.lower() == 'q':
            print("Goodbye!")
            break

        try:
            if sides == "":
                sides = 6  # Default to a 6-sided dice if no input
            else:
                sides = int(sides)

            result = roll_dice(sides)
            print(f"The dice rolled: {result}")
        except ValueError:
            print("Please enter a valid number of sides.")

# Run the dice roller
if __name__ == "__main__":
    main()
