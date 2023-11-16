from colorama import Fore, Style, init  # Colorama for color and style
import random

init(autoreset=True)

"""
Questions in the game.
"""
# Questions in the game.
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
    },
    {
        "question": "What do you find hidden under the dusty furniture?",
        "options": ["An old photograph", "A hidden passage"],
        "answer": 1
    },
    {
        "question": "As you enter the kitchen, what do you hear behind you?",
        "options": ["Footsteps", "Whispers"],
        "answer": 0
    },
    {
        "question": "In the dimly lit hallway, what catches your attention?",
        "options": ["A flickering candle", "A mysterious painting"],
        "answer": 1
    },
    {
        "question": "What do you feel when you touch the cold doorknob?",
        "options": ["A static shock", "A sudden chill"],
        "answer": 0
    },
    {
        "question": "What appears in the dusty mirror as you pass by?",
        "options": ["A reflection of someone else", "A distorted face"],
        "answer": 1
    },
    {
        "question": "What do you see in the abandoned nursery?",
        "options": ["Toys scattered on the floor", "A rocking chair moving"],
        "answer": 1
    },
    {
        "question": "What do you smell in the hidden cellar?",
        "options": ["Musty dampness", "Freshly baked bread"],
        "answer": 0
    },
    {
        "question": "As you climb the creaky stairs, what do you hear above?",
        "options": ["Giggling", "A distant piano melody"],
        "answer": 1
    },
    {
        "question": "What catches your eye in the dusty library?",
        "options": ["A glowing book", "A pair of glowing eyes"],
        "answer": 0
    },
    {
        "question": "What do you feel when you step into the cold cellar?",
        "options": ["A gust of wind", "A ghostly presence"],
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
    print("- You find yourself in a haunted mansion.")
    print("- Make choices to navigate through the haunted rooms.")
    print("- Every choice affects the outcome.")
    print("- Get the correct answer to escape the paranormal.")
    print("- Three wrong answers, and the ghost catches you!")


def get_player_answer():
    """
    Get the player's answer (1 or 2) with input validation.
    """
    while True:
        try:
            user_input = input("Your choice: ").strip().lower()
            if user_input in ['1', '2']:
                return int(user_input)
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError as e:
            print(f"Error: {e}")


def play_game(questions, difficulty):
    random.shuffle(questions)
    selected_questions = questions[:7]
    score = 0
    wrong_answer = 0

    if difficulty == 'easy':
        # Allow more wrong answers
        max_wrong_answers = 4
    elif difficulty == 'medium':
        max_wrong_answers = 3
    elif difficulty == 'hard':
        # Allow fewer wrong answers for higher difficulty
        max_wrong_answers = 2
    else:
        print("Invalid difficulty level. Defaulting to medium.")
        max_wrong_answers = 3

    for q in selected_questions:
        print(q["question"])

        for i, option in enumerate(q["options"]):
            print(f"{i + 1}. {option}")

        user_input = get_player_answer()

        answer = q["answer"] + 1
        if answer == user_input:
            print(Fore.GREEN + "Correct answer!\n" + Style.RESET_ALL)
            score += 1
            wrong_answer = 0
        else:
            print(Fore.RED + "The ghost gets closer..\n" + Style.RESET_ALL)
            wrong_answer += 1

        if wrong_answer == max_wrong_answers:
            print(Fore.RED + "The Ghost caught you!.\n" + Style.RESET_ALL)
            return

    print(Fore.GREEN + "You got away!\n" + Style.RESET_ALL)
    print(f"The game is over. Your score: {score}/{len(selected_questions)}")


if __name__ == "__main__":
    """
    Start the game.
    """
    def main():
        try:
            present_story()

            while True:
                print("1. Start Game")
                print("2. Read Rules")
                print("3. Difficulty Levels")
                print("4. Quit")

                choice = input("Enter your choice: ")

                if choice == '1':
                    difficulty = input("(easy, medium, hard): ").lower()
                    play_game(questions, difficulty)
                elif choice == '2':
                    display_rules()
                elif choice == '3':
                    print("Difficulty Levels:")
                    print("1. Easy")
                    print("2. Medium")
                    print("3. Hard")
                    difficulty_choice = input("Level (1, 2, 3): ").lower()
                    if difficulty_choice == '1':
                        difficulty = 'easy'
                    elif difficulty_choice == '2':
                        difficulty = 'medium'
                    elif difficulty_choice == '3':
                        difficulty = 'hard'
                    else:
                        raise ValueError("Invalid choice. Medium difficulty.")
                    play_game(questions, difficulty)
                elif choice == '4':
                    print("Thanks for playing my game. Goodbye!")
                    break
                else:
                    raise ValueError("Invalid choice. Enter 1, 2, 3, or 4.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    main()