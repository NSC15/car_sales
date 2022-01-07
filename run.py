import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('car_sales')
stock_worksheet = SHEET.worksheet("car_stock_sheet")
certified_stock = SHEET.worksheet("certified_stock_list")
honda_filter = certified_stock.range("honda")




print("""
'    _   _  _____    _____          _____     _____         _      ______  _____ 
'   | \ | |/ ____|  / ____|   /\   |  __ \   / ____|  /\   | |    |  ____|/ ____|
'   |  \| | |      | |       /  \  | |__) | | (___   /  \  | |    | |__  | (___  
'   | . ` | |      | |      / /\ \ |  _  /   \___ \ / /\ \ | |    |  __|  \___ \ 
'   | |\  | |____  | |____ / ____ \| | \ \   ____) / ____ \| |____| |____ ____) |
'   |_| \_|\_____|  \_____/_/    \_\_|  \_\ |_____/_/    \_\______|______|_____/ 
'                                                                                
'                                                                                
""")
print("\nWelcome to NC Car Sales Command Line Program. \n")
name = input("Please enter your name : ")
print("\nHello there " + name)


def get_user_details():
    """
    Function for the user to input which section they wish to purse
    Ran on a while loop so that validate user function can loop as intended
    """
    while True:
        print("\nPlease choose from either Customer Section or Staff Section")
        user = input("\n'1' for Customer Section | '2' for Staff Section : ")
        if validate_user(user):
            break
    return user


def validate_user(choice):
    """
    validate that user has entered an integer,
    and that the integer is either 1 or 2
    run appropriate function based on upser input or return error
    if input is not 1 or 2
    """
    try:
        choice = int(choice)
    except ValueError as e:
        print(f"Please enter an integer, you entered {e} ")
        return False
    else:
        if choice == 1:
            read_car_stock()
        elif choice == 2:
            new_car_stock()
        elif choice != 1 or 2:
            print(f"Please enter a valid input, you entered {choice}")
            return False
    return True


def read_car_stock():
    """
    function reads data from google sheet
    """
    print(colored("\nWelcome to the Customer Section", "yellow"))
    print(colored("\nWe have a variety of Japanese Cars in stock", "yellow"))
    print(colored("\nPlease choose the appropriate filter", "yellow"))
    print(colored("Enter '1' to view Honda's", "yellow"))
    print(colored("Enter '2' to view Toyota's", "yellow"))
    print(colored("Enter '3' to view Subaru's", "yellow"))
    print(colored("Enter '4' to view Mitsubishi's", "yellow"))
    print(colored("Enter '5' to view Mazda's", "yellow"))
    user_filter =  \
        input(colored("\nPlease enter your desired filter: ", "green"))
    validate_filter(user_filter)

def validate_filter(user_filter):
    try:
        user_filter = int(user_filter)
    except ValueError as e:
        print(f"Please enter a valid option, you entered {e}")
    else:
        if user_filter == 1:
            for i in honda_filter:
                print(i.value)


def new_car_stock():
    """
    User inputs new car stock, input is split,
    for make and model on google sheet,
    which then updates the car_stock_worksheet
    by adding this car. Again, on a while loop for data validation
    """
    print(colored("\nYou are in the Staff section", "blue"))
    new_car = input(colored("\nEnter new car Manufacturer & Model: ", "blue"))
    stock_addition = new_car.split()
    print(f"You have successfully added {new_car}")
    stock_worksheet.append_row(stock_addition)
    staff_multiple_entry()
  

def staff_multiple_entry():
    """
    loop to allow user to enter another car or return to menu
    linked with function validate_return_staff which includes
    function parameters
    """
    while True:
        print(colored("\nTo enter another car enter '1'", "blue"))
        print(colored("To return to the menu enter '2'", "blue"))
        return_staff = input(colored("Please enter your choice : "))
        if validate_return_staff(return_staff):
            break
    return return_staff


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
            print(colored("\n...returning you to beginning of program", "red"))
            get_user_details()
        elif staff_choice != 1 or 2:
            print(colored("\nYou entered an incorrect option...", "red"))
            return False
    return True



get_user_details()




