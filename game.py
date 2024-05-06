from HangmanTemplates import HangmanTemplates
import getpass

class game:
    def game(self):
        flag = False
        while flag == False:
            n_players = input("Enter the number of players (1 or 2): ")
            if n_players == "1" or n_players == "2":
                flag = True
            else:
                print("Invalid input - Enter 1 or 2")
                continue
        correct_letters = []
        incorrect_letters = []
        incorrect_words = []
        n_fails = 0
        game_over = False

        if n_players == "1":
            wordToGuess = HangmanTemplates.getAnimalWords()
        else :
            wordToGuess = input("Enter a word for player 2 to guess: ")

        print("Word to guess: " + "_" * len(wordToGuess))

        while game_over == False:
            hangmanVisual =  HangmanTemplates.get_guesses(n_fails + 1)
            print(hangmanVisual)

            for letter in wordToGuess:

                if letter in correct_letters:
                    print(letter, end="")
                else:
                    print("_", end=" ")
            print()
            print("For a list of letters still to guess type 'help' or type 'quit' to quit")
            guess = input("Guess a letter or a word : ")

            if guess == "help":
                self.game_help(correct_letters, incorrect_letters, incorrect_words, n_fails, game_over, wordToGuess)
                continue


            if guess == "quit":
                game_over = self.game_quit()
                break

            if len(guess) > 1:
                if guess in incorrect_words:
                    print("You already guessed that word - try again")
                    continue
                else:
                    if guess == wordToGuess:

                        game_over = self.game_won()
                        break

            if guess in incorrect_letters or guess in correct_letters:
                print("You already guessed that letter - try again")
                continue
            else:

                if guess in wordToGuess and len(guess) == 1:
                    print("Correct")
                    correct_letters.append(guess)

                    wordToGuessRemoved = []
                    wordToGuessRemoved = list(wordToGuess)

                    if all(letter in correct_letters for letter in wordToGuess):
                        game_over = self.game_won()
                        break

                elif len(guess) < 1:
                        print("Please make a guess at a letter or a word")
                        continue
                else:
                    print("Wrong")
                    n_fails = n_fails + 1
                    if len(guess) == 1:
                        incorrect_letters.append(guess)
                    else:
                        incorrect_words.append(guess)

            if n_fails == 6:
                print("Game over")
                print("The word was: " + wordToGuess)
                hangmanVisual =  HangmanTemplates.get_guesses(n_fails + 1)
                print(hangmanVisual)
                game_over = True


    def game_help(self, correct_letters, incorrect_letters, incorrect_words, n_fails, game_over, wordToGuess):
        letters_to_guess = HangmanTemplates.get_unused_letters(correct_letters + incorrect_letters)
        sorted_letters = " ".join(sorted(letters_to_guess))
        print("Letters left to guess: " + sorted_letters)
        print("Letters already guessed: " + " ".join(sorted(incorrect_letters + correct_letters)).upper())
        if incorrect_words != []:
            print("Words that have already been guessed: " + " ".join(sorted(incorrect_words)).upper())

    def game_quit(self):
        print("Goodbye")
        game_over = True
        return game_over

    def game_won(self):
        print("Correct, You have guessed the word!")
        print("You Won")
        game_over = True
        return game_over