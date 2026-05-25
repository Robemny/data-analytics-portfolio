# Robemny Bautista

# Function to show instructions
def show_instructions():
    print("Escape the Data Lab")
    print("Collect all items before entering the Control Room.")
    print("Commands:")
    print("  go North, go South, go East, go West")
    print("  get item")


# Function to show player status
def show_status(current_room, inventory, rooms):
    print("\n---------------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)

    # Show item in room (if exists and not villain)
    if 'item' in rooms[current_room] and rooms[current_room]['item'] != 'AI':
        print("You see a", rooms[current_room]['item'])


def main():

    # Dictionary linking rooms and items
    rooms = {
        'Lobby': {'North': 'Server Room', 'South': 'Security Office', 'East': 'Visualization Lab', 'West': 'Data Storage'},
        'Data Storage': {'East': 'Lobby', 'item': 'USB Drive'},
        'Server Room': {'South': 'Lobby', 'item': 'Server Key'},
        'Visualization Lab': {'West': 'Lobby', 'item': 'Dashboard Report'},
        'Security Office': {'North': 'Lobby', 'South': 'Coding Room', 'item': 'Security Badge'},
        'Coding Room': {'North': 'Security Office', 'South': 'Break Room', 'item': 'Python Script'},
        'Break Room': {'North': 'Coding Room', 'South': 'Network Hub', 'item': 'Energy Drink'},
        'Network Hub': {'North': 'Break Room', 'South': 'Control Room', 'item': 'Network Map'},
        'Control Room': {'North': 'Network Hub', 'item': 'AI'}  # villain
    }

    current_room = 'Lobby'
    inventory = []

    show_instructions()

    # Gameplay loop
    while True:

        show_status(current_room, inventory, rooms)

        move = input("Enter your move: ")

        # Move command
        if move.lower().startswith("go "):
            direction = move[3:].capitalize()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")

        # Get item command
        elif move.lower() == "get item":

            if 'item' in rooms[current_room]:
                item = rooms[current_room]['item']

                # Check if villain
                if item == 'AI':
                    if len(inventory) == 7:
                        print("\nCongratulations! You shut down the AI and escaped!")
                    else:
                        print("\nGAME OVER! The AI caught you before you were ready.")
                    break

                # Add item
                else:
                    inventory.append(item)
                    print(item, "collected!")
                    del rooms[current_room]['item']

            else:
                print("No item in this room.")

        # Invalid command
        else:
            print("Invalid input.")

    print("Thanks for playing.")


# Run the game
main()