import random


def choose_word():
    """Choose a random word

    Returns:
    str: random word from list words"""
    words = ['python', 'java', 'javascript', 'php']
    return random.choice(words)


# while True:
#     word = random.choice(words)
#     display_word = word[:3] + '-' * (len(word) - 3)
#     print("Guess the word", display_word, ":", end='')
#     guess = input().lower()
#     if guess == word:
#         print("You survived!")
#         break
#     else:
#         print("You lost!")

def display_word_with_guesses(word, guessed_letters):
    """Display the word with correctly guessed letters

    Parameters:
    word(str): random word has been chosen
    guessed_letters(list): list of letters that has been guessed correctly

    Returns:
    str: word with guessed letters"""
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '-'
    return display_word


def menu():
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: ')
        if choice == "play":
            word = choose_word()
            display_word = '-' * len(word)
            attempts = 8
            guessed_letters = []

            print("HANGMAN")

            while attempts > 0:
                print(f"\n{display_word}")
                guess = input("Input a letter: ").lower()

                # if guess in guessed_letters:
                #     print("No improvements")
                #     attempts -= 1
                #     if "-" not in display_word:
                #         break
                #     continue

                if guess in guessed_letters:
                    print("You've already guessed this letter")

                guessed_letters.append(guess)

                if guess in word:
                    display_word = display_word_with_guesses(word, guessed_letters)
                else:
                    print("That letter doesn't appear in the word.")
                    attempts -= 1
                if "-" not in display_word:
                    print("You guessed the word!\n"
                          "You survived")
                    break

            if attempts == 0:
                print("You lost!")

        elif choice == "exit":
            break


menu()
# print("""Thanks for playing!
# We'll see how well you did in the next stage.""")
