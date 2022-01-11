import gspread
from google.oauth2.service_account import Credentials
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
honda = SHEET.worksheet("Honda")
toyota = SHEET.worksheet("Toyota")
subaru = SHEET.worksheet("Subaru")
mitsubishi = SHEET.worksheet("Mitsubishi")
mazda = SHEET.worksheet("Mazda")
password = "carsales"

dfhonda = pd.DataFrame(honda.get_all_records())
dftoyota = pd.DataFrame(toyota.get_all_records())
dfsubaru = pd.DataFrame(subaru.get_all_records())
dfmitsubishi = pd.DataFrame(mitsubishi.get_all_records())
dfmazda = pd.DataFrame(mazda.get_all_records())

car_to_dataframe_mapper = {
    1: dfhonda, 2: dftoyota, 3: dfsubaru, 4: dfmitsubishi, 5: dfmazda
}