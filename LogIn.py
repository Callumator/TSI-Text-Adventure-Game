from CustomerLoad import CustomerLoad
from ReadDB import database_manager

dbManager = database_manager()

class LogIn:
    def get_password(self,customer):
        password = input("Enter your password: ")
        if password == customer[3]:
            return True
        else:
            return False
        return password

    def get_email(self, email_address):
        customerLoad = dbManager.get_users()
        for customer in customerLoad:
            if email_address == customer[0]:
                print("Email in Database")
                return customer

        print("Email not in Database")
        return None

    def log_in(self):
        flag = False
        while flag == False:
            email_address = input("Enter your email address: ")
            customer = self.get_email(email_address)
            if customer == None:
                print("It appears that that email address is not in our database")
                continue
            else:
                flag = True
        flag = False
        attempts = 0
        while flag == False and attempts <= 3:
            password = self.get_password(customer)
            if password == False:
                print("Wrong password, you have " + str(3 - attempts) + " attempts left")
                attempts += 1
                continue
            else:
                print("You have successfully logged in")
                flag = True

        return flag

class SignUp:
    def sign_up(self):
        signed_up = False
        while signed_up == False:
            Continue = False
            email_address = input("Enter your email address for signing up: ")
            for customer in dbManager.get_users():
                if email_address == customer[0]:
                    print("That email address is already in our database")
                    Continue = True
            if Continue == True:
                continue
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            password = input("Enter your password: ")
            dbManager.insert_user(email_address, first_name, last_name, password)
            signed_up = True
