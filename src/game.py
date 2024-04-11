from HangmanTemplates import HangmanTemplates

class game:
    def players1():

        correct_letters = []
        incorrect_letters = []
        incorrect_words = []
        n_fails = 0
        game_over = False
        wordToGuess = HangmanTemplates.getAnimalWords()

        print("Word to guess: " + "_" * len(wordToGuess))

        while game_over == False:
            hangmanVisual =  HangmanTemplates.get_guesses(n_fails + 1)
            print(hangmanVisual)

            for letter in wordToGuess:

                if letter in correct_letters:
                    print(letter, end="")
                else:
                    print("_", end=" ")

            print("For a list of letters still to guess type 'help'")
            guess = input("Guess a letter or a word or 'quit': ")

            if guess == "help":
                print("Letters left to guess: " + str(set(HangmanTemplates.letters_used()) - set(correct_letters)))
                continue


            if guess == "quit":
                print("Goodbye")
                game_over = True
                break

            if len(guess) > 1:
                if guess in incorrect_words:
                    print("You already guessed that word - try again")
                    continue
                else:
                    if guess == wordToGuess:
                        print("Correct")
                        print("You Won")
                        game_over = True
                        break
                    else:
                        print("Wrong")
                        n_fails = n_fails + 1
                        incorrect_words.append(guess)

            if guess in incorrect_letters or guess in correct_letters:
                print("You already guessed that letter - try again")
                continue
            else:

                if guess in wordToGuess:
                    print("Correct")
                    correct_letters.append(guess)
                    if "".join(correct_letters) == wordToGuess:
                        print("You won")
                        game_over = True
                        break
                else:
                    print("Wrong")
                    n_fails = n_fails + 1
                    incorrect_letters.append(guess)
                    print("Number of fails: " + str(n_fails))

            if n_fails == 7:
                print("Game over")
                print("The word was: " + wordToGuess)
                game_over = True





    def players2():

        playerWon = False
        print("NOT FINISHED YET")


