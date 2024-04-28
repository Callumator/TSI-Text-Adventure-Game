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

        # customerLoad = ReadDB()
        # customers = dbManager.get_users()
        # password = ""
        # counter = 0
        # while password == "" and counter < len(customers):
        #     if email_address == customers[counter].get_email():
        #         password = customers[counter].password
        #     counter += 1
        return password

    def get_email(self, email_address):
        customerLoad = dbManager.get_users()
        for customer in customerLoad:
            if email_address == customer[0]:
                print("in customerLoad")
                return customer

        print("not in cutomerLoad")
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
            # if email_address 
            #     print("That email address is already in our database")
            #     continue
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            password = input("Enter your password: ")
            dbManager.insert_user(email_address, first_name, last_name, password)
            signed_up = True
