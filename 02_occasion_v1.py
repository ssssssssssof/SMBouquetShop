# ask user for occasion
def user_occasion():
        occasion = input("What is the occasion for this bouquet? ")
        
        # if response is blank, output will result in error
        if occasion.strip() == "":
            print("\nError: Occasion cannot be blank. Please try again.\n")
        # if response is not "Valentine's Day," output will result in error
        elif occasion != "Valentine's Day":
            print("\nError: Invalid occasion. Only Valentine's Day is supported. Please try again.\n")
        else:
            print("\nYou selected the occasion: " + occasion)
            input("\nPress Enter to continue...")

# main routine
user_occasion()