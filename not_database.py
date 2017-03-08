import csv
import os

class User:

    def __init__(self, user_name, password, full_name, destination):
        self.user_name = user_name
        self.password = password
        self.full_name = full_name
        self.destination = destination

    def __repr__(self):
        return "\nusername: {}\n password: {}\n name: {}\n destination: {}\n".format(self.user_name, self.password, self.full_name, self.destination)

    def see_info(self):
        print(self)

    def add_new_user(self):
        with open("travel_plans.csv", "a") as csvfile:
             csvfile.write("{},{},{},{}\n".format(self.user_name, self.password, self.full_name, self.destination))
        csvfile.close()

    def is_valid_credentials(self, username, password):
        return self.user_name == username and self.password == password


def clear():
    os.system("clear")

def check_login(login_name, login_password):
    current_users = []
    yes_user = []
    with open("travel_plans.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            u = User(*row)
            current_users.append(u)
    for user in current_users:
        if user.is_valid_credentials(login_name, login_password):
            print("\nHere is your info: ")
            print(user)
            return user
    return None


#def check_login(login_name, login_password):
    # current_users = []
    # yes_user = []
    # with open("travel_plans.csv", 'r', newline='') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')
    #     for row in reader:
    #         current_users.append(row)
    # for info_list in current_users:
    #     if info_list[0] == login_name and info_list[1] == login_password:
    #         yes_user.append(info_list)
    # if yes_user:
    #     return True
    # else:
    #     return False


def main():
    #success = 0
    print("\n*Welcome to Travel Info*\n")
    while True:
        current_user = None
        while not current_user:
            login_name = input("Press [q] to quit. \n\nWhat is your username? ").lower()
            if login_name == 'q':
                exit()
            login_password = input("Enter your password: ")
            current_user = check_login(login_name, login_password)
            if current_user:
                print("You have successfully logged in.")
                #success += 1
            else:
                print("Incorrect username or password. Try again.") # make loop to let them try again
        while current_user:
            #show_user_info(login_name, login_password)
            user_choice = input("[C]reate new user or [L]og out? ").lower()
            if user_choice == 'c':
                new_username = input("Please enter new username: ")
                new_password = input("Please enter new password: ")
                new_fullname = input("What is your full name? ")
                new_destination = input("Where would you like to travel next? ")
                new_user = User(new_username, new_password, new_fullname, new_destination)
                new_user.add_new_user()
                clear()
                print("Your information has been saved.")

            elif user_choice == 'l':
                clear()
                current_user = None
                #success -= 1
                break

main()
