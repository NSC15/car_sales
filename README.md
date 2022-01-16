# NC Car Sales Command Line Program

## Live Link - <https://nc-car-sales.herokuapp.com/>

![CLI image](assets/images/CLI.png)

## Background

The Car sales is my third Milestone Project, this time using Python to create a CLI which uses an API to access data from an external Google sheet with cars for sale details,
this program allows the user to access two sides to the program, the customer side which is viewing available stock of cars from a fictional Japanese based car dealership, or the
staff section which requires a password to enter ("carsales") and then allows the user to enter a car into the database. The program has several loops and data validation to create
a fully accessible application.

## User Experience (UX)

### User Story & Target Audience

#### First Time Visitor Goals

- I want to be able to enter some personal namely detail
- I want to be able to define what type of user i am, and access the relevant part
- I want to be able to access cars for sale data (customer)
- I want to be able to filter the cars i want to see
- I want to be able to login and access protected parts of the program
- I want to be able to input new stock into the program

#### Target Audience

- The Target Audience for this APP is aimed at but not limited to anyone which would be looking to buy a car from this fictional car dealership. The app is made in a way to be multi-functional
by being able to choose which user route you want to go down at the beginning of the program.

## Design

### Colour Scheme

- Due to this being a terminal, design is limited.
- I have used different font colours to improve readability and group text subjects into colours.

### Font

- I have added ASCII Art into the CLI for the main loading text, again to spruce up the terminal. With the intention to provide a unique user interface.

- Different font colours are used throughout the terminal, which have been imported from the python library TermColor

## Layout and Functionality of the CLI

### The first terminal loading stage -

- You are greeted with the ASCII Art Car Sales logo as such, with then an input to enter your name as the user,
this input will only accept alphabetical characters either lowercase or uppercase as programmed by the developer for validation.

- The user then gets recognition that their name has been entered via the print message, which
then leads on to a user choice to determine their intentions, customer section or staff
section?

### Customer Section

- User has chosen option 1 to enter the customer section, the program then displays introductory text, telling
the user they are in this section, and the appropriate filters they can choose for make of car they are
interested in, lastly the input is then waiting for the users choice

- If a valid option has been chosen a DataFrame will be displayed, which reads the data from the API of stock
available and certain details about the cars, however if an invalid filter is entered then the program tells the
user to enter a valid option (program to loop until a valid option is entered). Finally, the user is then prompted with the choice of viewing more cars and returning to the start (providing full navigation through the
program with needing to restart the terminal)

- Once an entry is entered via the Staff Section, this should then be displayed in the relevant filter on this
section, as the new data will be pulled through via the API

### Staff Section

- User has chosen option 2 for the Staff Section, this then requires a password to semi-emulate a real life
application. Please Note the password is "carsales". The program will check the password, and deny entry if
the entered password is incorrect.

- Once into the staff section, the user is then prompted with the instructions and an example of how to enter
the data into the program to send to the external source (google sheet) via the API. The program is designed to
check for the correct amount of enteries to stop missing data being added.

## WireFrames

- No Wireframe created for this project due it being a terminal based application.

## Features

- Inputs
- Input Validation
- Loops
- Read API Data
- Write Data via API
- Controlled Errors

## Future Improvements

- Extensive filtering (by engine / price)
- Larger database to hold any make of car

## Back-End Data Source

- I have used a Google sheet and linked my program to read / write data with

## Technologies

- Termcolor - Used to implement coloured text into my terminals design
- Pandas - Data Processing library, used DataFrames to display my API data.
- gspread - Used to connect up Google Sheets
- re - Used for validating user inputs when declaring name variable

## Testing

- Auto Testing - Completed by PEP8, returned with no errors
- Manual Testing - Manual testing completed in development stages as well as on the deployed version.
- Testing completed after each function was coded to maintain working code, and identify bugs early in able to fix efficiently.
- Responsive testing not needed in this project as app is targeted at desktop users only. However, app does work in multiple browsers
tested in Google Chrome and Mozilla FireFox.

## Bugs

- API car filter only displaying five rows of data - As standard .head() function only prints 5 rows of data unless
specifically set to a value. It is now set to 20, so if there is 20 rows of data this will display them all.
- Program crashing out at customer section when user gets chance to view another car or exit, if a user was to enter an invalid input instead of 1 or 2. Fix was to integrate a try / except to convert the input into an integer and if not, to raise a valueerror and return to the main section.
- Freshly inputted data not available to view without closing and restarting terminal - code source found
to restart program internally without breaking the terminal, custom code edited to suit change so program
not flows nicely, and allows user to return to the customer section and review their inputted data.


