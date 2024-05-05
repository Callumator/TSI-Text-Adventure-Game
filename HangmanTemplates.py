from random import randrange
class HangmanTemplates:

    def get_guesses(max_guesses):
        guess_templates = [
            """
  +---+
  |   |
      |
      |
      |
      |
=========""",
            """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
            """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
            """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
            """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
            """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
            """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
            ]
        return '\n'.join(guess_templates[max_guesses-1:max_guesses])
    def get_unused_letters(used_letters):
        ALPHABETARRAY= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        list_of_unused_letters = []

        for letter in used_letters:
            if letter.upper() in ALPHABETARRAY:
                ALPHABETARRAY.remove(letter.upper())

        return ALPHABETARRAY


    def getAnimalWords():
        ANIMALWORDS = [
            "ant",
            "baboon",
            "badger",
            "bat",
            "bear",
            "beaver",
            "camel",
            "cat",
            "clam",
            "cobra",
            "coyote",
            "crow",
            "deer",
            "dog",
            "donkey",
            "duck",
            "eagle",
            "ferret",
            "fox",
            "frog",
            "goat",
            "goose",
            "hawk",
            "lion",
            "lizard",
            "llama",
            "mole",
            "monkey",
            "moose",
            "mouse",
            "mule",
            "newt",
            "otter",
            "owl",
            "panda",
            "parrot",
            "pigeon",
            "python",
            "rabbit",
            "ram",
            "rat",
            "raven",
            "rhino",
            "salmon",
            "seal",
            "shark",
            "sheep",
            "skunk",
            "sloth",
            "snake",
            "spider",
            "stork",
            "swan",
            "tiger",
            "toad",
            "trout",
            "turkey",
            "turtle",
            "weasel",
            "whale",
            "wolf",
            "wombat",
            "zebra"
        ]

        return ANIMALWORDS[randrange(len(ANIMALWORDS))]

