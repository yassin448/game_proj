import time
import random


# --- Utility Functions ---


def simulate_typing(response, t):
    """Simulates typing effect for the given response string."""
    for char in response:
        print(char, end="", flush=True)
        time.sleep(random.uniform(0.02, 0.08))
    print()
    time.sleep(t)


def check_for_input_choice(valid_choices):
    """
    Prompts the user until a valid choice is entered.
    Returns the valid integer choice.
    """
    while True:
        try:
            # input([1,2])
            # input([1,2])
            choice = int(
                input(
                    f"What would you like to do? (1,2)"
                    f"({'/'.join(map(str, valid_choices))}): "
                )
            )
            # Check if the choice is in the valid choices
            if choice in valid_choices:
                return choice
            print(f"Invalid choice.")
            print(f"Please choose from {valid_choices}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# --- Game Location Handlers ---


def house():
    """Handles the house encounter sequence."""
    simulate_typing("You enter the house and find it empty.", 2)
    simulate_typing("Suddenly, a wicked fairie appears!", 2)
    simulate_typing(
        "You fight bravely, but with only your dagger, " "you are no match.", 2
    )
    simulate_typing("You barely escape with your life.", 2)


def cave():
    """Handles the cave encounter and sword discovery."""
    global inventory
    simulate_typing("You enter the cave and find a treasure chest.", 2)
    simulate_typing("Inside the chest, you find a magical sword!", 2)
    inventory["sword"] = True
    simulate_typing("You feel empowered.", 2)


def forest():
    """Handles the forest encounter with conditional outcome."""
    global inventory
    simulate_typing("You walk into the forest and hear rustling.", 2)
    if inventory["sword"]:
        simulate_typing("A wild wolf appears.You defeat it with sword.", 2)
        simulate_typing("You find a rare herb that restores your strength.", 2)
        inventory["herb"] = True
    else:
        simulate_typing("A wild wolf attacks. You escape,you're injured", 2)


def river():
    """Handles the river encounter and amulet retrieval."""
    global inventory
    simulate_typing("You approach the river and see something shiny.", 2)
    simulate_typing("You dive in and retrieve an enchanted amulet!", 2)
    inventory["amulet"] = True
    simulate_typing("It glows warmly in your hands.", 2)


def mountain():
    """Handles the mountain encounter and wisdom gain."""
    global inventory
    simulate_typing("You climb the mountain and meet a sage.", 2)
    simulate_typing("He teaches you the secret to resisting dark magic.", 2)
    inventory["wisdom"] = True


# --- Game Logic ---


def reset_game():
    """Resets the player's inventory and score for a new game."""
    global score, inventory
    simulate_typing("Resetting game state...", 2)
    score = 0
    inventory = {"sword": False, "amulet": False, "wisdom": False, "herb": False}
    simulate_typing("Score and inventory have been reset.", 1)
    simulate_typing("You are now at the beginning of your adventure.", 2)


def final_battle():
    """Handles the final battle scenario."""
    global score, inventory
    simulate_typing(
        "You return to the field. " "The wicked fairie emerges from the shadows!", 2
    )

    if inventory["sword"]:
        simulate_typing("You draw your magical sword.", 2)
    else:
        simulate_typing("You only have your dagger. This won't end well...", 2)

    if inventory["amulet"]:
        simulate_typing("Your amulet shields you from dark magic.", 2)

    if inventory["wisdom"]:
        simulate_typing("You recall the sage's teachings and focus.", 2)

    if all(inventory[k] for k in ["sword", "amulet", "wisdom"]):
        simulate_typing(
            "With sword, amulet, and wisdom, "
            "you defeat the fairie in an epic battle! You Win!",
            2,
        )
        score += 3
    elif inventory["sword"] and inventory["amulet"]:
        simulate_typing("You strike hard and resist the fairie's magic.", 2)
        simulate_typing("She retreats, wounded. You’ve won.", 2)
        score += 1
    else:
        simulate_typing("The fairie overwhelms you with magic and speed.", 2)
        simulate_typing("You are defeated. Game Over!", 2)
        score -= 1

    simulate_typing(f"Final Score: {score}", 2)


def story_core():
    """Main game loop allowing location choices and tracking visits."""
    options = {
        1: ("Enter the house", house),
        2: ("Enter the cave", cave),
        3: ("Explore the forest", forest),
        4: ("Approach the river", river),
        5: ("Climb the mountain", mountain),
        6: ("Face the fairie", final_battle),
    }
    while True:
        simulate_typing("\nWhere would you like to go?", 1)
        for key, (desc, _) in options.items():
            if key != 6:
                simulate_typing(f"{key}. {desc}", 1)
        simulate_typing("6. Face the fairie (only if you're ready)", 1)

        choice = check_for_input_choice(list(options.keys()))
        desc, action = options[choice]

        if choice == 6:
            final_battle()
            break
        else:
            action()


def main():
    """Entry point of the game loop."""
    simulate_typing("Welcome to the text-based adventure game!", 2)
    while True:
        simulate_typing("1. Start a new game", 2)
        simulate_typing("2. Exit", 2)
        usr_input = check_for_input_choice([1, 2])
        if usr_input == 1:
            reset_game()
            story_core()
        elif usr_input == 2:
            simulate_typing("Thank you for playing! GoodBye!", 2)
            break
        else:
            simulate_typing("Invalid choice.Please try again.", 2)


score = 0
inventory = {"sword": False, "amulet": False, "wisdom": False, "herb": False}
if __name__ == "__main__":
    main()
