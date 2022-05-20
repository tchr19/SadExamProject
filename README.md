# Exam Management System - SAD exam

## Project description
This is the code for the program attached to the SAD exam project. The project involves designing a new exam management system, and programming the backend data structures for it.

The main file includes classes from two separate documents, the exam and the user class, and contains some functions which were meant to be hidden away in other classes, such as the authorization functions.

For future work, properly employing the wrapper pattern to implement authorization would be a priority. Furthermore switching the list of registered users, to a list of dictionaries, which can be appended when users are registered, also needs to be implemented.

## How to run the code
Currently the code is mostly hardcoded. Mockups of the UI have been made, and can be found in the project report, but has not been programmed.

Four dummy users have been made, one for each role.
* Student credentials:
    * Username: student
    * Password: student
* Teacher credentials:
    * Username: teacher
    * Password: teacher
* Censor credentials:
    * Username: censor
    * Password: censor
* Secretary credentials:
    * Username: secretary
    * Password: secretary

When running the program from main, the program prompts to input username and password in the terminal. The program prints if the login was successful or not.