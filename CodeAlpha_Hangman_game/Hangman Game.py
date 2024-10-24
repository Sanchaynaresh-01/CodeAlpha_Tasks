import random

def choose_word():
    words = ["python", "hangman", "programming", "development", "challenge","Compete","Smart"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |  
           |
        """,
        """
           -----
           |   |
           |   O
           |  
           |  
           |
        """,
        """
           -----
           |   |
           |  
           |  
           |  
           |
        """,
        """
           -----
           |   |
           |   
           |  
           |  
           |
        """,
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    tries = 5
    guessed_word = ['_'] * len(word)

    print("Welcome to Hangman!")

    while tries > 0 and '_' in guessed_word:
        print(display_hangman(tries))
        print("Current word: " + " ".join(guessed_word))
        print("Guessed letters: " + " ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower()  # Make guess lowercase

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word.lower():  # Check for guess in lowercase word
            for index, letter in enumerate(word):
                if letter.lower() == guess:  # Case-insensitive comparison
                    guessed_word[index] = letter
            print("Good guess!")
        else:
            tries -= 1
            print("Incorrect guess! You have " + str(tries) + " tries left.")

    if '_' not in guessed_word:
        print("Congratulations! You've guessed the word: " + word)
    else:
        print(display_hangman(tries))
        print("Sorry, you've run out of tries. The word was: " + word)

if name == "main":  # Correct the typo
    play_hangman()