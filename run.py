import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored
import pandas as pd



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
honda = SHEET.worksheet("Honda")
toyota = SHEET.worksheet("Toyota")
subaru = SHEET.worksheet("Subaru")
mitsubishi = SHEET.worksheet("Mitsubishi")
mazda = SHEET.worksheet("Mazda")

dfhonda = pd.DataFrame(honda.get_all_records())
dftoyota = pd.DataFrame(toyota.get_all_records())
dfsubaru = pd.DataFrame(subaru.get_all_records())
dfmitsubishi = pd.DataFrame(mitsubishi.get_all_records())
dfmazda = pd.DataFrame(mazda.get_all_records())







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
    user can input which section they wish to pursue
    while loop to move onto next function if 'validate_user' function 
    returns true.
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
    customer section, displays instructions to user for filtering results
    prompts an input 'user_filter' which is then given to the validate function
    all code within a while loop, to stop if the input is acceptable -
    determined by the 'validate_filter' function.
    """
    while True:
        print(colored("\nYou are in the Customer Section", "yellow"))
        print(colored("\nWe have a variety of Japanese Cars in stock", "yellow"))
        print(colored("\nPlease choose the appropriate filter", "yellow"))
        print(colored("Enter '1' to view Honda's", "yellow"))
        print(colored("Enter '2' to view Toyota's", "yellow"))
        print(colored("Enter '3' to view Subaru's", "yellow"))
        print(colored("Enter '4' to view Mitsubishi's", "yellow"))
        print(colored("Enter '5' to view Mazda's", "yellow"))
        user_filter =  \
            input(colored("\nPlease enter your desired filter: ", "green"))
        if validate_filter(user_filter):
            break
    return user_filter

def validate_filter(user_filter):
    """
    Pulls and displays range of data from API (Google Sheet) based on user choice.
    Validates that an input is of the correct type (integer), 
    and only accepts inputs between 1 and 5 as per instructions displayed.
    """
    
    
    try:
        user_filter = int(user_filter)
    except ValueError as e:
        print(f"Please enter a valid option, you entered {e}")
        return False
    else:
        if user_filter == 1:
            print(dfhonda.head())
        elif user_filter == 2:
            print(dftoyota.head())
            
        elif user_filter == 3:
            print(dfsubaru.head())
        elif user_filter == 4:
            print(dfmitsubishi.head())
        elif user_filter == 5:
            print(dfmazda.head())
        elif user_filter not in range(1,5):
            print(colored("\nPlease enter a valid option from the above", "red"))
            return False
    return True    


def new_car_stock():
    """
    User inputs new car stock, input is split,
    for make and model on google sheet,
    which then updates the car_stock_worksheet
    with the input.
    While loop used for data validation and continuation.
    """
    print(colored("\nYou are in the Staff section", "blue"))
    new_car = input(colored("\nEnter new car Manufacturer & Model: ", "blue"))
    stock_addition = new_car.split()
    print(f"You have successfully added {new_car} to the stocklist")
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




#hondas = ' - '.join([str(i.value) for i in honda_filter])
 #               car = hondas[0:4]
  #              print("ID:" + car)