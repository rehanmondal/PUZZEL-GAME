import random as rd
import word_lists as wl

word = rd.choice(wl.words)

chances = 5
guessed_word = "_"*len(word)

print("\n\n ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ LETTER GUESSING PUZZEL GAME  ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")

while chances != 0:
    print("\t\t\t\t\t\t", guessed_word)
    guessed_letter = input("Guess the letter : ").lower()
    if guessed_letter in word:
        for i in range(len(word)):
            if word[i] == guessed_letter:
                guessed_word = guessed_word[:i]+guessed_letter + guessed_word[i+1:]
                # print(guessed_word)

        if guessed_word == word:  # this is the random word that is choosen randomly
            print("You Won ! ")
            break

    else:
        chances = chances - 1
        print("Uhh ! Wrong Guess !! \nRemaining Chanches - ",chances)

else:
    print("Game Over")

print("The Correcr Game is ",word)



