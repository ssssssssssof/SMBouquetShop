# import modules
import time

# ask user for occasion
def user_occasion():
    while True:
        occasion = input("What is the occasion for this bouquet? ")
        # if response is blank, output will result in error
        if occasion.strip() == "":
            print("\nError: Occasion cannot be blank. Please try again.\n")
        # if response is not "valentine's day," output will result in error
        elif occasion != "Valentine's Day":
            print("\nError: Invalid occasion. Only Valentine's Day is supported. Please try again.\n")
        else:
            print("\nYou selected the occasion: " + occasion)
        # add a delay of 1 second after printing occasion
            time.sleep(1) 
        # prompts user to press Enter to continue
            input("\nPress Enter to continue...")
            break

# main routine
user_occasion()

