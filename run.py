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


print("Welcome to NC Car Sales Command Line Program. \n")
name = input("Please enter your name : ")
print("\nHello there " + name)


def get_user_details():
    """
    function to get the users status to run different functions depending
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


def new_car_stock():
    """
    User inputs new car stock, input is split
    for make and model on google sheet,
    which then updates the car_stock_worksheet
    by adding this car
    """
    print(colored("\nWelcome to the Staff section", "blue"))
    new_car = input(colored("\nEnter new car Manufacturer & Model): ", "blue"))
    stock_addition = new_car.split()
    print(f"You have successfully added {new_car}")
    stock_worksheet = SHEET.worksheet("car_stock_sheet")
    stock_worksheet.append_row(stock_addition)


get_user_details()
