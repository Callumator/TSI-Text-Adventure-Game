from HangmanTemplates import HangmanTemplates


class game:
    def players1():
        n_fails = 0
        playerWon = False
        while playerWon == False:
            wordToGuess = HangmanTemplates.getAnimalWords()
            hangmanVisual =  HangmanTemplates.get_guesses(n_fails + 1)
            print(hangmanVisual)
            playerWon = True


    def players2():

        playerWon = False
        print("NOT FINISHED YET")


