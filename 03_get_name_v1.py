# ask user for name
def get_name(question):
    while True:
        response = input(question)
        # if name is blank, output will result in error
        if response == "":
            print("Error: Name cannot be blank. Please try again.")
        else:
            return response

def get_valid_name():
    print("\nPlease enter the gift receiver's name")
    name = get_name("Name: ")
    print("\nGreat! We're currently building " + name + "'s bouquet. Won't be a moment...")

# main routine
get_valid_name()
