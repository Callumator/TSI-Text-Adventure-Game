from LogIn import LogIn
from game import game


class Main:
    def main():
        log_in = LogIn()
        log_in.log_in()
        flag = False
        while flag == False:
            n_players = input("Enter number of players (1 or 2) or quit: ")
            if n_players == "1":
                print("One player game")
                flag = True
                game.players1()

            elif n_players == "2":
                print("Two players game")
                flag = True
                game.players2()

            elif n_players == "quit":
                print("Goodbye")
                break

            else:
                print("Invalid input - Enter number of players (1 or 2) or quit: ")


if __name__ == '__main__':
    Main.main()

