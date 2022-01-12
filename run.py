import re
from termcolor import colored
from constants import (PASSWORD, honda, toyota, subaru, mitsubishi, mazda,
                       car_to_dataframe_mapper)


# -------- Initiation of program -------
print("""
   ___             __       _          
  / __\__ _ _ __  / _\ __ _| | ___ ___ 
 / /  / _` | '__| \ \ / _` | |/ _ / __|
/ /__| (_| | |    _\ | (_| | |  __\__ \\
\____/\__,_|_|    \__/\__,_|_|\___|___/
""")
print(colored("\nWelcome to NC Car Sales Command Line Program.\n", "cyan"))
while True:
    name = input("Please enter your name : ")
    if re.search(r'^[a-zA-z]+$', name):
        break
print("\n")
print(colored(f"Hello there {name}", "cyan"))

# -------- User Choice -------#


def get_user_details():
    """
    user can input which section they wish to pursue
    while loop to move onto next function if 'validate_user' function
    returns true.
    """
    while True:
        print("\nPlease choose from either Customer Section or Staff Section")
        user =  \
            input("\n'1' for Customer | '2' for Staff: ")
        if validate_user(user):
            break
    return user

# ------- User Choice Data Validation -------


def validate_user(choice):
    """
    validate that user has entered an integer,
    and that the integer is either 1 or 2
    run appropriate function based on upser input or return error
    if input is not 1 or 2
    """
    try:
        choice = int(choice)
        if choice > 2:
            raise ValueError(choice)
    except ValueError as e:
        print("\n")
        print(f"Please enter a valid integer, you entered {e} ")
        return False
    else:
        if choice == 1:
            read_car_stock()
        elif choice == 2:
            while True:
                print("\n")
                user_pass = \
                    input("Please enter Staff password: ")
                if user_pass == PASSWORD:
                    new_car_stock()
                    break
                else:
                    print(colored("\nPassword Incorrect", "red"))
                    continue
    return True

# ------- Customer Section / Read API Data --------


def read_car_stock():
    """
    customer section, displays instructions to user for filtering results
    prompts an input 'user_filter' which is then given to the validate function
    all code within a while loop, to stop if the input is acceptable -
    determined by the 'validate_filter' function.
    """
    while True:
        print(colored("\nYou are in the Customer Section", "yellow"))
        print(colored("\nWe have a variety of Cars in stock", "yellow"))
        print(colored("\nPlease choose the appropriate filter", "yellow"))
        print(colored("Enter '1' to view Honda's", "yellow"))
        print(colored("Enter '2' to view Toyota's", "yellow"))
        print(colored("Enter '3' to view Subaru's", "yellow"))
        print(colored("Enter '4' to view Mitsubishi's", "yellow"))
        print(colored("Enter '5' to view Mazda's", "yellow"))
        user_filter =  \
            input("\nPlease enter your desired filter: ")
        if validate_filter(user_filter):
            break
    return user_filter

# ------- API Data Filter Validation --------


def validate_filter(user_filter):
    """
    Pulls and displays data from API (Google Sheet) based on user choice.
    Validates that an input is of the correct type (integer),
    and only accepts inputs between 1 and 5 as per instructions displayed.
    """      
    try:
        user_filter = int(user_filter)
    except ValueError as e:
        print(f"Please enter a valid option, you entered {e}")
        return False
    else:
        if user_filter >= 1 and user_filter <= 5:
            print(car_to_dataframe_mapper[user_filter].head(20))
            print("\nTo view more enter '1' to exit enter '2'")
            print("\nBe careful any other input will end the program!!\n")
            return_customer = input("Your Choice: ")
            return_customer = int(return_customer)
            if return_customer == 1:
                read_car_stock()
            elif return_customer == 2:
                print(colored("\n...logging out", "red"))
                get_user_details()
            else:
                print("\nIncorrect input - ... returning to menu")
                get_user_details()
                  
        else:
            print(colored("\nPlease enter a valid option", "red"))
            return False
    return True

# -------- Staff Section / Write Data to API source (Google Sheet)-------


def new_car_stock():
    """
    User inputs new car stock, input is split,
    for make and model on google sheet,
    which then updates the car_stock_worksheet
    with the input.
    While loop used for data validation and continuation.
    """
    print(colored("\nYou are in the Staff section", "green"))
    while True:       
        print(colored("\nPlease enter the following - ", "green"))
        print(colored("""
Make | Model | Variant | Colour | Engine | Condition | Price""", "green"))
        print("\nAll Lowercase | Include a space between entries")
        new_car = input("\nEnter new car : ")
        stock_addition = new_car.split()
        if len(stock_addition) == 7:
            break
        else:
            print(colored("\nPlease enter all required information", "red"))
            continue
    print(f"You added {new_car} to the stocklist")
    if "honda" in stock_addition:
        honda.append_row(stock_addition)
    elif "toyota" in stock_addition:
        toyota.append_row(stock_addition)
    elif "subaru" in stock_addition:
        subaru.append_row(stock_addition)
    elif "mitsubishi" in stock_addition:
        mitsubishi.append_row(stock_addition)
    elif "mazda" in stock_addition:
        mazda.append_row(stock_addition)
    staff_multiple_entry()

# ------- Staff Section / Continuation (Enter another or return)--------


def staff_multiple_entry():
    """
    loop to allow user to enter another car or return to menu
    linked with function validate_return_staff which includes
    function parameters
    """
    while True:
        print(colored("\nTo enter another car enter '1'", "blue"))
        print(colored("\nTo return to the menu enter '2'", "blue"))
        return_staff = input("\nPlease enter your choice : ")
        if validate_return_staff(return_staff):
            break
    return return_staff

# -------- Validation for Staff Section Continuation --------


def validate_return_staff(staff_choice):
    """
    validate that user has entered an integer,
    and that the integer is either 1 or 2.
    """
    try:
        staff_choice = int(staff_choice)
    except ValueError as e:
        print(f"Please enter an integer, you entered {e} ")
        return False
    else:
        if staff_choice == 1:
            new_car_stock()
        elif staff_choice == 2:
            print(colored("\n...logging out", "red"))
            get_user_details()
        elif staff_choice != 1 or 2:
            print(colored("\nYou entered an incorrect option...", "red"))
            return False
    return True


get_user_details()
