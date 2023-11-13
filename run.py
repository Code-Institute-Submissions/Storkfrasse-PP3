from colorama import Fore, Style, init

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
    border = "+" + "=" * 110 + "+"
    story = f"""
    {Fore.YELLOW}{border}{Style.RESET_ALL}
    {Fore.RED}|{'Whispers in the Shadows':^110}|{Style.RESET_ALL}
    {Fore.YELLOW}{border}{Style.RESET_ALL}
    """
    print(story)
    intro_text = """
    You find yourself in an old, decrepit mansion on a stormy night. 
    The air is thick with an eerie fog, and the only light comes from flickering candles lining the walls.
    Strange sounds echo through the empty halls, and you can't shake the feeling of being watched.

    As you explore further, you come across an ancient book with a forgotten spell.
    As you read the incantation aloud, the room changes, 
    and you realize you've awakened something supernatural. 
    The spirits of the mansion are now restless, 
    and you must navigate through the haunted rooms, 
    making decisions that will either lead to your escape or draw the paranormal closer.

    Beware, every choice you make affects the outcome. Do you have the courage to face the shadows and uncover 
    the mysteries hidden within?

    Now, brace yourself, and let the whispers guide you through the shadows...
    """
    print(intro_text)
    print(f"{Fore.YELLOW}{border}{Style.RESET_ALL}")


def play_game(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for i, option in enumerate(q["options"]):
            print(f"{i + 1}. {option}")
        answer = int(input("Your choice: ")) - 1
        if answer == q["answer"]:
            print(Fore.GREEN + "Correct answer!\n" + Style.RESET_ALL) # Green color for correct answer
            score += 1
        else:
            print(Fore.RED + "Wrong answer. The ghost gets closer...\n" + Style.RESET_ALL) # Red color for wrong answer
    print(f"The game is over. Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    """
    Start of the game
    """
    def main():
        present_story()
        play_game(questions)

    main()