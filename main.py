from LogIn import *
from game import game

game = game()
class Main:
    def main():
        signed_in = False

        while signed_in == False:
            login_or_signup = input("Enter 1 to log in or 2 to sign up or 'quit' to quit: ")

            if login_or_signup == "1":
                log_in = LogIn()
                successful_login = log_in.log_in()
                signed_in = True

            elif login_or_signup == "2":
                sign_up = SignUp()
                sign_up.sign_up()
                print("if you successfully signed up, now you can sign in using those details")

            elif login_or_signup == "quit":
                print("Goodbye")
                exit()
            else:
                print("Invalid input - Enter 1 to log in or 2 to sign up or 'quit' to quit: ")
        if successful_login == True:
            game.game()
        else:
            print("Unsuccessful Login. Goodbye")


if __name__ == '__main__':
    Main.main()

