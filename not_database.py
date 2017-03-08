import csv
import os

class User:

    def __init__(self, user_name, password, full_name, destination):
        self.user_name = user_name
        self.password = password
        self.full_name = full_name
        self.destination = destination

    def __repr__(self):
        return self.user_name, self.password, self.full_name, self.destination

    def see_info(self):
        print(self)

def clear():
    os.system("clear")

def show_user_info(login_name, login_password):
    current_users = []
    yes_user = []
    with open("travel_plans.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            current_users.append(row)
    for info_list in current_users:
        if info_list[0] == login_name and info_list[1] == login_password:
            yes_user.append(info_list)
    print("\nHere is your info: ")
    for single_list in yes_user:
        print("\nusername: {}\n password: {}\n name: {}\n destination: {}\n".format(single_list[0], single_list[1], single_list[2], single_list[3]))

def check_login(login_name, login_password):
    current_users = []
    yes_user = []
    with open("travel_plans.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            current_users.append(row)
    for info_list in current_users:
        if info_list[0] == login_name and info_list[1] == login_password:
            yes_user.append(info_list)
    if yes_user:
        return True
    else:
        return False

# def add_new_user(self):
#     with open("travel_plans", "w") as f:
#         new_user = [] "{},{},{},{}\n".format(self.user_name, self.password, self.full_name, self.destination)
#         f.write(new_user)
#     f.close()


def main():
    success = 0
    print("Welcome to travel database")
    while True:
        while success == 0:
            login_name = input("What is your username? ")
            login_password = input("Enter your password: ")
            if check_login(login_name, login_password) is True:
                print("You have successfully logged in.")
                success += 1
            else:
                print("Incorrect username or password. Try again.") # make loop to let them try again
        while success == 1:
            show_user_info(login_name, login_password)
            user_choice = input("[C]reate new user or [L]og out? ").lower()
            if user_choice == 'c':
                new_username = input("Please enter new username: ")
                new_password = input("Please enter new password: ")
                new_fullname = input("What is your full name? ")
                new_destination = input("Where would you like to travel next? ")
            elif user_choice == 'l':
                clear()
                success -= 1
                break

main()
