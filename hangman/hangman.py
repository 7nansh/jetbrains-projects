import random
import string
print("H A N G M A N")
while True:
    menu = input('Type "play" to play the game, "exit" to quit:')
    if menu == "play":
        print("")
        word = random.choice(['python', 'java', 'kotlin', 'javascript'])
        h_word = ["-" for _ in word]
        print("".join(h_word))
        tried_letter = []
        tries = 8
        while tries != 0:
            letter = input("Input a letter:")
            if letter in tried_letter:
                print("You've already guessed this letter")
                print("")
                print("".join(h_word))
                continue
            if len(letter) > 1 or len(letter) == 0:
                print("You should input a single letter")
                print("")
                print("".join(h_word))
                continue
            if letter not in string.ascii_lowercase:
                print("Please enter a lowercase English letter")
                print("")
                print("".join(h_word))
                continue
            tried_letter.append(letter)
            if letter in word:
                for i, e in enumerate(word):
                    if e == letter:
                        h_word[i] = letter
            else:
                print("That letter doesn't appear in the word")
                tries -= 1
            if tries == 0 and "-" in h_word:
                print("You lost!")
                break
            if "-" not in h_word:
                print("")
                print("".join(h_word))
                print("You guessed the word!")
                print("You survived!")
                break
            print("")
            print("".join(h_word))
    elif menu == "exit":
        break
    else:
        continue
