import random
#list with different words to guess
word_list = ["monkey", "crocodile", "penguin"]

#picks a random word from the word_list
chosen_word = random.choice(word_list)
print(chosen_word)

#asking player for a letter
guess = input("Guess a letter: ").lower()

#checks if the guessed letter matches the current letter in the word
for letter in chosen_word: 
    if letter == guess:
        print("Right!")
    else:              
        print("Wrong!")

