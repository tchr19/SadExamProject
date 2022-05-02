from xml.dom.pulldom import START_DOCUMENT
import user as u
#import profile as p
import exam as ex


client_user = str(input("Username: "))
client_pass = str(input("Password: "))
currentUser = None

users = [u.user('Poul', 1, 'student', 'student', 'student'), u.user('Pauline', 2, 'teacher', 'teacher', 'teacher'),u.user('Jens', 1, 'censor', 'censor', 'censor'),u.user('Kim', 1, 'secretary', 'secretary', 'secretary')]
#Exam type and grading scale are booleans; 0 = written and 7 step scale, 1 = oral and "pass or fail type"
#sadExam = ex.exam('SAD exam','SAD', 5, "02.06.2022", "Federico and Israel", 1, 1)

def login():
        for us in users:
            if client_user == us.get_username() and client_pass == us.get_password():
                #print('success')
                return us.get_ID(), us.get_role()                
            elif client_user != us.get_username() and client_pass != us.get_password():
                print('wrong')
                break #? Hvis man har break, fortæller den ikke hvor mange users der er

currentUser = login()
print(currentUser)

def veri(): #! Can this verification be moved to a class - in this case the user class? 
    for us in users:
        if currentUser[0]==us.get_ID():
            #print(us.get_name())
            return us.get_name() 
        
        #else:
            #print("????")

currentName = veri()
print(currentName)




# Example op tuple
#def operate(a, b):
#    sum = a + b
#    diff = a - b
#    mul = a * b
#    div = a / b
#    return sum, diff, mul, div
#



#Now you can call this function for two numbers and assign the return values to variables:
#
#n1 = 5
#n2 = 10
#sum, diff, mul, div = operate(n1, n2)
#print(
#    f"The sum is {sum}\n"
#    f"The difference is {diff}\n"
#    f"The multiplication gives {mul}\n"
#    f"The division gives {div}\n"
#)
#This results in the following being printed in the console:
#
#The sum is 15
#The difference is -5
#The multiplication gives 50
#The division gives 0.5