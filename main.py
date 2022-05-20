import user as u
import exam as ex


client_user = str(input("Username: "))
client_pass = str(input("Password: "))
currentUser = None

# users is a list containing all registered users. Dictionaries could be used here
# List should get appended everytime a user is registered
users = [u.user('Poul', 1, 'student', 'student', 'student'), u.user('Pauline', 2, 'teacher', 'teacher', 'teacher'),u.user('Jens', 3, 'censor', 'censor', 'censor'),u.user('Kim', 4, 'secretary', 'secretary', 'secretary')]


#Exam type and grading scale are booleans; 0 = written and 7 step scale, 1 = oral and "pass or fail type"
#sadExam = ex.exam('SAD exam','SAD', 5, "02.06.2022", "Federico and Israel", 1, 1)

def login(): # The login function loops through all registered users and compares credentials with clint input
        for us in users:
            if client_user == us.get_username() and client_pass == us.get_password():
                print('success')
                return us.get_ID(), us.get_role()                
            elif client_user != us.get_username() and client_pass != us.get_password():
                print('wrong')
                

currentUser = login() # Upon successful login, the user ID and role is saved in an array
print(currentUser)


# Function that checks if the user is a teacher.
# Similar functions for other roles should be made, and used in a wrapper to check for authorization when requesting to use a function
def checkAuthTeacher():
    for us in users:
        if currentUser[1] == 'teacher':
            return("access granted") # requested function should be slotted in here if said function should be accessed by a teacher
        else:
            return("access denied") # function to provide feedback that authorization should be made here


print(checkAuthTeacher())
