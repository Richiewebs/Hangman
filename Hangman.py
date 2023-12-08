print(f"          HANGMAN          ")
print(f"          -------          ")
import words

import random

stages = ['''
    +---+
    |   |
    o
    |   |
   / \  |
    |   |
   / \  |
        |
__________
__________ 

''', '''

    +---+
    |   |
    o
    |   |
   / \  |
    |   |
   /    |
        |
__________
__________ 

''', '''

     +---+
     |   |
     o
     |   |
    / \  |
     |   |
         |
         |
__________
__________ 
''', '''

    +---+
    |   |
    o
    |   |
   / \  |
        |
        |
        |
__________
__________ 
''', '''

    +---+
    |   |
    o
    |   |
   /    |
        |
        |
        |
__________
__________ 
''', '''

    +---+
    |   |
    o
    |   |
        |
        |
        |
        |
__________
__________ 
''']

ran = random.randint(0, len(words.word_list))

chosen_word = words.word_list[ran]

dash = "".split()
for i in chosen_word:
    dash += "_"
print(" ".join(dash))


end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in dash:
        print(f"You've already guessed {guess}")
    for i in chosen_word:
        if i == guess:
            for a in range(0, len(chosen_word)):
                if guess == chosen_word[a]:
                    dash[a] = guess
    print(" ".join(dash))
    if "_" not in dash:
        end_of_game = True
        print("You've won!")
    else:
        end_of_game = False
        if guess not in chosen_word:
            lives -= 1
            print(f"{guess} is not in the word.You lose a life")
            print(stages[lives])
            if lives == 0:
                print("you've lost")
                end_of_game = True
