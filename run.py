from colorama import Fore, Style, init  # Colorama for color and style

init(autoreset=True)

"""
Questions in the game.
"""
questions = [
    {
        "question": "What did you hear in the dark corner?",
        "options": ["A sound", "Nothing"],
        "answer": 0
    },
    {
        "question": "What did you see in the mirror?",
        "options": ["Your own reflection", "A shadow"],
        "answer": 1
    },
    {
        "question": "What did you find in the old book?",
        "options": ["A forgotten spell", "Blank pages"],
        "answer": 0
    },
    {
        "question": "In the abandoned room, what caught your eye?",
        "options": ["A flickering candle", "A ghostly figure"],
        "answer": 1
    },
    {
        "question": "What did you smell in the eerie fog?",
        "options": ["Decaying leaves", "Roses"],
        "answer": 0
    },
    {
        "question": "What sound echoed in the haunted mansion?",
        "options": ["Creaking floorboards", "Laughter"],
        "answer": 0
    },
    {
        "question": "What did you touch in the hidden chamber?",
        "options": ["A cold metal key", "Warm sunlight"],
        "answer": 1
    }
]


def present_story():
    """
    Story intro
    """
    border = "+" + "=" * 50 + "+"
    story = f"""
    {Fore.YELLOW}{border}{Style.RESET_ALL}
    {Fore.RED}|{'Whispers in the Shadows':^50}|{Style.RESET_ALL}
    {Fore.YELLOW}{border}{Style.RESET_ALL}
    """
    print(story)
    intro_text = """
    You find yourself in an old, decrepit mansion on a stormy night.
    The air is thick with an eerie fog,
    and the only light comes from flickering candles lining the walls.
    Strange sounds echo through the empty halls,
    and you can't shake the feeling of being watched.

    As you explore further, you come across an ancient book with
    a forgotten spell.
    As you read the incantation aloud, the room changes,
    and you realize you've awakened something supernatural.
    The spirits of the mansion are now restless,
    and you must navigate through the haunted rooms,
    making decisions that will either lead to your escape or
    draw the paranormal closer.

    Beware, every choice you make affects the outcome.
    Do you have the courage to face the shadows and uncover
    the mysteries hidden within?

    Now, brace yourself, and let the whispers guide you through the shadows...
    """
    print(intro_text)
    print(f"{Fore.YELLOW}{border}{Style.RESET_ALL}")


def display_rules():
    print("\nRules:")
    print("- You find your self in a haunted mansion.")
    print("- Make choices to navigate through the haunted rooms.")
    print("- Every choice affect the outcome.")
    print("- Get the correct answer to escape the paranormal.")
    print("- Three wrong answers, and the ghost catches you!")
    


def play_game(questions):
    score = 0
    wrong_answer = 0

    for q in questions:
        print(q["question"])

        for i, option in enumerate(q["options"]):
            print(f"{i + 1}. {option}")

        while True:
            user_input = input("Your choice: ")
            # Check if the input is not empty
            if user_input.strip() and user_input.strip() in ['1', '2']:
                break
            else:
                print("Invalid input. Please enter 1 or 2.")

        answer = q["answer"] + 1
        if answer == int(user_input):
            # Green color for correct answer
            print(Fore.GREEN + "Correct answer!\n" + Style.RESET_ALL)
            score += 1
            # Reset the wrong answer counter on a correct answer
            wrong_answer = 0
        else:
            # Red color for wrong answer
            print(Fore.RED + "The ghost gets closer..\n" + Style.RESET_ALL)
            wrong_answer += 1

        if wrong_answer == 3:
            print(Fore.RED + "The Ghost caught you!.\n" + Style.RESET_ALL)
            # Exit the function and the game
            return

    print(Fore.GREEN + "You got away!\n" + Style.RESET_ALL)
    print(f"The game is over. Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    """
    Start of the game
    """
    def main():
        present_story()

        while True:
            print("1. Start Game")
            print("2. Read Rules")
            print("3. Quit")

            choice = input("Enter your choice:")

            if choice == '1':
                play_game(questions)
            elif choice == '2':
                display_rules()
            elif choice == '3':
                print("Thanks for playing my game. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    main()