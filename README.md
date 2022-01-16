# NC Car Sales Command Line Program

## Live Link - <https://nc-car-sales.herokuapp.com/>

![CLI image](assets/images/CLI.png)

## Background

The NC Car Sales App is my third Milestone Project, this time using Python to create a CLI which uses an API to read and write data from an external Google sheet with car details,
this program allows the user to access two sides to the program, the customer side which is viewing available stock of cars from a fictional Japanese based car dealership, or the
staff section which requires a password to enter (password = "carsales") and then allows the user to enter a car into the database. The program has several loops and data validation to create
a fully navigational application.

## User Experience (UX)

### User Story & Target Audience

#### First Time Visitor Goals

- I want to be able to define what type of user i am, and access the relevant section
- I want to be able to access cars for sale data (customer)
- I want to be able to filter the cars i wish to view.
- I want to be able to login and access protected parts of the program (staff section)
- I want to be able to input new stock into the program

#### Returning Visitor Goals

- I want to view latest available cars
- I want to add new car stock to the database

#### Target Audience

- The Target Audience for this APP is aimed at but not limited to anyone which would be looking to buy a car from this fictional car dealership, or alternatively, any member of staff required to input new stock entries for customer viewing.
- The app is made in a way to be multi-functional by being able to choose which user route you want to go down at the beginning of the program.

## Design

### Colour Scheme

- Due to this being a terminal, design is limited unlike front-end projects.
- I have used different font colours to improve readability and group text subjects into colours.

### Font

- I have added ASCII Art into the CLI for the main loading text, again to spruce up the terminal. With the intention to provide a unique user interface.

- Different font colours are used throughout the terminal, which have been imported from the python library TermColor

## Layout and Functionality of the CLI

### The first terminal loading stage -

- You are greeted with the ASCII Art Car Sales logo as such, with then an input to enter your name as the user,
this input will only accept alphabetical characters either lowercase or uppercase as programmed by the developer for validation.

- The user then gets recognition that their name has been entered via a print message, which
then leads on to a user choice to determine their intentions, customer section or staff
section?

### Customer Section

- User has chosen option 1 to enter the customer section, the program then displays introductory text, telling
the user they are in this section, and the appropriate filters they can choose from for the make of car they are
interested in.

- If a valid option has been chosen a DataFrame will be displayed, which reads the data from the API of stock
available and certain details about the cars, however if an invalid filter is entered then the program tells the
user to enter a valid option (program to loop until a valid option is entered). Finally, the user is then prompted with the choice of viewing more cars or returning to the start (providing full navigation through the
program without needing to restart the whole terminal)

- Once a new entry is entered via the Staff Section, this should then be displayed in the relevant filter on this
section, as the new data will be pulled through via the API.

### Staff Section

- User has chosen option 2 for the Staff Section, this then requires a password to semi-emulate a real life
application. Please Note the password is "carsales". The program will check the password, and deny entry if
the entered password is incorrect.

- Once into the staff section, the user is then prompted with the instructions and an example of how to enter
the data into the program to send to the external source (google sheet) via the API. The program is designed to
check for the correct amount of entries to stop missing data being added. If the user enters a non-recognised manufacturer the program will say so and provide another chance to enter valid data or restart the program.

## WireFrames

- No Wireframe created for this project due it being a terminal based application.

## Features

- Inputs
- Input Validation
- Loops
- Read API Data
- Write Data via API
- Controlled Errors
- Internal Restart Function

## Future Improvements

- Extensive filtering (by engine / price for example)
- Larger database to hold any make of car

## Data Model

- I have used a Google sheet and linked my program to read / write data.

## Technologies

- Termcolor - Used to implement coloured text into my terminals design
- Pandas - Data Processing library, used DataFrames to display my API data.
- gspread - Used to connect up Google Sheets
- re - Used for validating user inputs when declaring name variable
- sys - Used for the ability to manipulate runtime environment
- os - Used for accessing file directory.
- Constants - External local constants file

## Testing

- Auto Testing - Completed by PEP8, returned with no errors
- Manual Testing - Manual testing completed in development stages as well as on the deployed version.
- Testing completed after each function was created to maintain working code, and identify bugs early in able to fix efficiently.
- Responsive testing not needed in this project as app is targeted at desktop users only. However, app does work in multiple browsers.
- Manually tested in Google Chrome and Mozilla FireFox.

## Bugs

- API car filter only displaying five rows of data - As standard .head() function only prints 5 rows of data unless
specifically set to a value. It is now set to 20, so if there is 20 rows of data this will display them all.
- Program crashing out at customer section when user gets chance to view another car or exit, function expects input of 1 or 2, bug occurred when a string was inputted. Fix was to integrate a try / except to convert the input into an integer and if not, to raise a ValueError and return to the main section.
- Freshly inputted data not available to view without closing and restarting terminal - code source found
to restart program internally without breaking the terminal, custom code edited to suit change so program
now flows properly, and allows user to return to the customer section and review their inputted data.
- Several advisory problems with the ASCII art addition on run.py, however these have no detrimental effect to the program so as a result these have been
acceptable for the visual benefits they create to the final product.

## Credits

- Slack - Community of like-minded students to bounce ideas off
- Reuben Ferante - CI Mentor for project reviews and improvement ideas
- DaniWeb - Sourced code for a function within development.
- PatorJK - ASCII Art source

## Deployment

### My project deployment

- This project is deployed via Heroku
- My project was created in Gitpod
- Git was used for Version Control
- My project was deployed once I had completed the majority of manual testing.

### Deploying Via Heroku

- You will require an account to access Heroku
- On the dashboard click "New" and then "Create New App"
- Assign your app a relative name and choose your appropriate region
- Create App
- Access setting from the tabs bar, central to the screen
- Reveal Config Vars
- Add the following - PORT : 8000 / CREDS : {your creds file e.g google sheet creds file}
- Now "Add Buildpack"
- It is imperative you add "Python" first, and then "nodejs" then click save.
- Now access the Deploy section on the main tabs bar
- Select Github (in this case) then Connect to Github
- Gain access to your GitHub account and search for the relevant repo you wish to deploy.
- You can now choose to Enable Automatic Deploys (recommended), this will then deploy your changes
once you have pushed to github. Otherwise it will mean manually deploying the project each time,
the choice is yours but for ease of development, automatic would be recommended for a non-industry project.
- The site will then provide feedback your app has been deployed and you can open it, if you wish.
- Tutorials can be found online e.g [Heroku Deployment Tutorial](https://youtu.be/KD9OaryS1Kw)

### Forking a Repository

- Forking is a good utility to use to make a copy of an original repository so that this can be edited without making any changes to the original development repository.

- Locate a repository you wish to copy

- The Fork button is above the repository control bar to the right.

- Once clicked this will then create the repository copy to your Github account.

### Cloning a Repository

- You can clone a repository straight to Gitpod if needed.

- Locate a repository you wish to clone

- Just below the repository control bar, there is a green Gitpod button.

- This will then open the project in Gitpod for you (if gitpod is installed).
