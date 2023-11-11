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
    }
]

"""
Question section
"""
def play_game(questions):
    score = 0
    for q in questions:
        print(q["question"])
        for i, option in enumerate(q["options"]):
            print(f"{i + 1}. {option}")
        answer = int(input("Your choice: ")) - 1
        if answer == q["answer"]:
            print("Correct answer!\n")
            score += 1
        else:
            print("Wrong answer. IT gets closer...\n")
    print(f"The game is over. Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    """
    Start of the game
    """
    def main():
        print("Whispers in the Shadows")
        play_game(questions)

    main()