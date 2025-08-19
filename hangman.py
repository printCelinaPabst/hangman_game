def Hangman():
    import json
    from functions import get_words
    import random

    easy, mid, hard = get_words()

    #game Title
    print("Welcome to Hangman!🕹️\n")

    while True:
        #ask player for gaming mode
        print("""Select a mode:\n
        1 -> Easy mode
        2 -> Mid Mode
        3 -> Hard Mode\n""")

        mode_choice = int(input("Type here: "))

        #picks a random word based of mode choice and set initial number of lives for the player
        if mode_choice == 1:
            chosen_word = random.choice(easy)
            lives = 3
        elif mode_choice == 2:
            chosen_word = random.choice(mid)
            lives = 5
        elif mode_choice == 3:
            chosen_word = random.choice(hard)
            lives = 6

        #Create list with underscores matching the word length
        placeholder = list("_" * len(chosen_word))

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
                print(chosen_word)
                print("Congratulations!🙌")
                print("You won the game!")
                break

            #Player loses if there are no more lives left
            if lives == 0:
                print("You lost the game😵‍💫")
                print(f"Your word was {chosen_word}\n")
                break
        #----------------------------------------------

        #ask player for another round 
        new_round = input("Try again?(y/n)").strip().lower()
        if new_round != "y":
            print()
            print("Thanks for playing!")
            print("See you next time!👋")
            break

Hangman()