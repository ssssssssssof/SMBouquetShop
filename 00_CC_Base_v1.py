# import modules go here *************************
import time
import re

# functions go here *************************

# function to display the title and purpose
def greet_user():
    print("\nWelcome to Build a Bouquet 💐")
    print("Build a bouquet for your loved ones for every occasion.\n")


# function to ask the user for their occasion
def user_occasion():
    while True:
        occasion = input("What is the occasion for this bouquet? ")
        # if response is blank, output will result in error
        if occasion.strip() == "":
            print("\nError: Occasion cannot be blank. Please try again.\n")
        # if response is not "valentine's day," (case-insensitive) output will result in error
        elif not re.search(r"valentine's day", occasion, re.IGNORECASE):
            print("\nError: Invalid occasion. Only Valentine's Day is supported. Please try again.\n")
        else:
            print("\nYou selected the occasion: " + occasion)
        # add a delay of 1 second after printing occasion
            time.sleep(1) 
        # prompts user to press Enter to continue
            input("\nPress Enter to continue...")
            break


# function to ask user for name
def get_name(question):
    while True:
        response = input(question)
        # if name is blank, output will result in error
        if response.strip() == "":
            print("Error: Name cannot be blank. Please try again.")
        else:
            return response

# function to ask user to enter gift receiver's name
def get_valid_name():
    print("\nPlease enter the gift receiver's name")
    name = get_name("Name: ")
    # print gift receiver's name
    print("\nGreat! Let's get to building " + name + "'s bouquet.")


# main routine *********************
greet_user()
user_occasion()
get_valid_name()
