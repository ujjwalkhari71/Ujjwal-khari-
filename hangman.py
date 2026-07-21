import random

WORDS = ["python", "hangman", "laptop", "science", "keyboard"]


def display_board(wrong_guesses, guessed_letters, word):
    """Display the word progress and wrong guesses."""
    print(f"\n  Wrong guesses left: {6 - wrong_guesses}")
    print(f"  Wrong letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\n  Word: {display_word}\n")


def get_guess(guessed_letters):
    """Prompt the user for a valid, new letter guess."""
    while True:
        guess = input("  Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("  Please enter a single letter.")
        elif not guess.isalpha():
            print("  Please enter a valid letter (a-z).")
        elif guess in guessed_letters:
            print(f"  You already guessed '{guess}'. Try another.")
        else:
            return guess


def play_hangman():
    """Main function to run the Hangman game."""
    print("=" * 40)
    print("        HANGMAN GAME")
    print("=" * 40)

    # Pick a random word
    word = random.choice(WORDS)

    guessed_letters = []   # list of all guessed letters
    wrong_guesses = 0      # count of incorrect guesses
    max_wrong = 6

    print(f"\n  A word has been chosen ({len(word)} letters). Good luck!\n")

    # Main game loop
    while wrong_guesses < max_wrong:
        display_board(wrong_guesses, guessed_letters, word)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(f"  ✓ '{guess}' is in the word!")

            # Check if player has won
            if all(letter in guessed_letters for letter in word):
                display_board(wrong_guesses, guessed_letters, word)
                print("=" * 40)
                print(f"  🎉 YOU WIN! The word was '{word}'")
                print("=" * 40)
                break
        else:
            wrong_guesses += 1
            print(f"  ✗ '{guess}' is NOT in the word!")

            if wrong_guesses == max_wrong:
                display_board(wrong_guesses, guessed_letters, word)
                print("=" * 40)
                print(f"  💀 GAME OVER! The word was '{word}'")
                print("=" * 40)


def run():
    """Run the game and offer replay."""
    while True:
        play_hangman()
        again = input("\n  Play again? (yes / no): ").lower().strip()
        if again != "yes":
            print("\n  Thanks for playing Hangman! Goodbye!")
            break
        print("\n" + "=" * 40)


# Entry point
run()