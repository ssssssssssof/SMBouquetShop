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

# main routine
get_valid_name()