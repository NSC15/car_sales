import gspread
from google.oauth2.service_account import Credentials

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
print(f"Hello there {name}")

def get_user_details():
    """
    function to get the users status to run different functions depending
    """
    while True:
        user = input("Please enter '1' for Customer or '2' for Staff : ")
        
        if validate_user(user):
            print("you entered a correct user, program running")
            break
    
    return user


def validate_user(choice):
    try:
        choice = int(choice)
    except ValueError as e:
        print(f"Please enter an integer, you entered {e} ")
        return False
    
    return True










get_user_details()