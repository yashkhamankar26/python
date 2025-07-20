import random


word_list = ["apple", "grape", "peach", "lemon", "mango"]

secret_word = random.choice(word_list)
guessed_word = ["_"] * len(secret_word)


guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Word Guessing Game!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses. Good luck!\n")

while wrong_guesses < max_wrong_guesses and "_" in guessed_word:
    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
        print("Good guess!\n")
    else:
        wrong_guesses += 1
        print(f"Wrong guess! You have {max_wrong_guesses - wrong_guesses} tries left.\n")


if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Out of guesses! The word was:", secret_word)
