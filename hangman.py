import random

#game Title
print("Welcome to Hangman!🕹️\n")

#list with different words to guess
word_list = ["monkey", "crocodile", "penguin"]

while True:

    #picks a random word from the word_list
    chosen_word = random.choice(word_list)

    #Create list with underscores matching the word length
    placeholder = list("_" * len(chosen_word))

    #Set initial number of lives for the player
    lives = 5

    #asking player for a letter
    while lives > 0:
        print()

        #prints a new unknown word
        print("".join(placeholder))
        guess = input("Guess a letter: ").lower()
    #-------------------------------------------

        #update list if guess is correct
        for i in range(len(chosen_word)):
                if guess == chosen_word[i]:
                        placeholder[i] = guess

        #if the guessed letter is wrong player loses a life
        if guess not in chosen_word:
            lives -= 1
            print("You lost a life...hang in there!💪")
            print(f"Lives left:{lives}\n")

        #Player wins if all letters are revealed and lives remain
        if "_" not in placeholder and lives > 0:
            print()
            print("Congratulations!🙌")
            print("You won the game!")
            break

        #Player loses if there are no more lives left
        if lives == 0:
            print("You lost the game😵‍💫")
            break
    #----------------------------------------------

    #ask player for another round 
    new_round = input("Try again?(y/n)").strip().lower()
    if new_round != "y":
        print()
        print("Thanks for playing!")
        print("See you next time!👋")
        break

