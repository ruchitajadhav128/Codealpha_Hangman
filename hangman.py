import random
import os


# ==============================
# COLORS
# ==============================

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"


# ==============================
# CLEAR SCREEN
# ==============================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ==============================
# HANGMAN DRAWING
# ==============================

def display_hangman(wrong):

    stages = [

        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,

        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """
    ]

    print(RED + stages[wrong] + RESET)


# ==============================
# GAME HEADER
# ==============================

def display_header():

    print(CYAN + BOLD)

    print("╔══════════════════════════════════════╗")
    print("║          🎯 HANGMAN GAME             ║")
    print("║      Guess the word to win!          ║")
    print("╚══════════════════════════════════════╝")

    print(RESET)


# ==============================
# PLAY GAME
# ==============================

def play_game():

    # 5 predefined words
    words = [
        "python",
        "computer",
        "school",
        "program",
        "keyboard"
    ]

    # Select random word
    word = random.choice(words)

    guessed_letters = []

    wrong_guesses = 0

    max_wrong = 6


    # ==============================
    # GAME LOOP
    # ==============================

    while wrong_guesses < max_wrong:

        clear_screen()

        display_header()

        # Display hangman
        display_hangman(wrong_guesses)


        # ==============================
        # DISPLAY WORD
        # ==============================

        display_word = ""

        for letter in word:

            if letter in guessed_letters:
                display_word += letter.upper() + " "

            else:
                display_word += "_ "


        print(
            BOLD +
            "WORD: " +
            RESET +
            YELLOW +
            display_word +
            RESET
        )


        # ==============================
        # DISPLAY LIVES
        # ==============================

        remaining = max_wrong - wrong_guesses

        print()

        print(
            BOLD +
            "❤️  Lives: " +
            RESET +
            GREEN +
            "♥ " * remaining +
            RESET +
            RED +
            "♡ " * wrong_guesses +
            RESET
        )


        # ==============================
        # GUESSED LETTERS
        # ==============================

        print()

        if guessed_letters:

            print(
                BOLD +
                "🔤 Guessed: " +
                RESET +
                ", ".join(
                    guessed_letters
                )
            )

        else:

            print(
                BOLD +
                "🔤 Guessed: " +
                RESET +
                "None"
            )


        # ==============================
        # CHECK WIN
        # ==============================

        if all(
            letter in guessed_letters
            for letter in word
        ):

            print()

            print(GREEN + BOLD)

            print("╔══════════════════════════════════════╗")
            print("║          🎉 YOU WON! 🎉              ║")
            print("╚══════════════════════════════════════╝")

            print(RESET)

            print(
                "The word was: " +
                YELLOW +
                word.upper() +
                RESET
            )

            return


        # ==============================
        # USER INPUT
        # ==============================

        print()

        print(CYAN + "─" * 40 + RESET)

        guess = input(
            BOLD +
            "👉 Enter a letter: " +
            RESET
        ).lower().strip()


        # ==============================
        # INPUT VALIDATION
        # ==============================

        if len(guess) != 1:

            print()

            print(
                RED +
                "❌ Please enter only ONE letter!" +
                RESET
            )

            input("\nPress Enter to continue...")

            continue


        if not guess.isalpha():

            print()

            print(
                RED +
                "❌ Please enter an alphabet letter!" +
                RESET
            )

            input("\nPress Enter to continue...")

            continue


        # ==============================
        # CHECK DUPLICATE
        # ==============================

        if guess in guessed_letters:

            print()

            print(
                YELLOW +
                "⚠️ You already guessed this letter!" +
                RESET
            )

            input("\nPress Enter to continue...")

            continue


        # Add letter to list
        guessed_letters.append(guess)


        # ==============================
        # CHECK GUESS
        # ==============================

        if guess in word:

            print()

            print(
                GREEN +
                BOLD +
                "✅ Correct guess!" +
                RESET
            )

        else:

            wrong_guesses += 1

            print()

            print(
                RED +
                BOLD +
                "❌ Wrong guess!" +
                RESET
            )


        input("\nPress Enter to continue...")


    # ==============================
    # GAME OVER
    # ==============================

    clear_screen()

    display_header()

    display_hangman(wrong_guesses)

    print(RED + BOLD)

    print("╔══════════════════════════════════════╗")
    print("║          💀 GAME OVER 💀             ║")
    print("╚══════════════════════════════════════╝")

    print(RESET)

    print(
        "The correct word was: " +
        YELLOW +
        word.upper() +
        RESET
    )


# ==============================
# MAIN PROGRAM
# ==============================

while True:

    clear_screen()

    display_header()

    print(BOLD + "Choose an option:" + RESET)

    print()

    print(GREEN + "1." + RESET + " 🎮 Start Game")
    print(RED + "2." + RESET + " 🚪 Exit")

    print()

    choice = input(
        BOLD +
        "Enter your choice: " +
        RESET
    )


    if choice == "1":

        play_game()

        print()

        again = input(
            CYAN +
            "Do you want to play again? (y/n): " +
            RESET
        ).lower()

        if again != "y":

            print()

            print(
                MAGENTA +
                "Thanks for playing! 👋" +
                RESET
            )

            break


    elif choice == "2":

        print()

        print(
            MAGENTA +
            "Thanks for playing Hangman! 👋" +
            RESET
        )

        break


    else:

        print()

        print(
            RED +
            "❌ Invalid choice! Please select 1 or 2." +
            RESET
        )

        input("\nPress Enter to continue...")