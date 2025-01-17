import random

def show_hangman(wrong_guesses):
    stages = [
        """
          -----
          |   |
              |
              |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
              |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
          |   |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
         /|   |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
              |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
         /    |
              |
        --------
        """,
        """
          -----
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        --------
        """,
    ]
    return stages[wrong_guesses]

def hangman_game():
    words_and_hints = [
        ("python", "A popular programming language."),
        ("pizza", "A cheesy delight often topped with pepperoni."),
        ("ocean", "A vast body of saltwater."),
        ("rainbow", "A colorful arc that appears after rain."),
        ("elephant", "The largest land animal."),
    ]

    chosen_word, hint = random.choice(words_and_hints)
    guessed_letters = set()
    wrong_guesses = 0
    max_guesses = 6

    print("Welcome to Hangman!")
    print(f"Here's your hint: {hint}")

    while wrong_guesses < max_guesses:
        print(show_hangman(wrong_guesses))
        current_word = [letter if letter in guessed_letters else "_" for letter in chosen_word]
        print("Current Word: " + " ".join(current_word))

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Oops! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
        elif guess in chosen_word:
            print(f"Great! '{guess}' is in the word.")
            guessed_letters.add(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            guessed_letters.add(guess)
            wrong_guesses += 1

        if all(letter in guessed_letters for letter in chosen_word):
            print("Congrats! You've guessed the word!")
            print(f"The word was: {chosen_word}")
            break
    else:
        print(show_hangman(wrong_guesses))
        print("Game Over! Better luck next time.")
        print(f"The word was: {chosen_word}")

hangman_game()
