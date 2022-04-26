#Imports the csv library allowing me to open and read and write to a csv file
import csv

#These lines of code open the usernames csv file and read the items into an array called userarray
usernames = r'usernames.csv'
with open(usernames)as userfile:
    userreader = csv.reader(userfile, skipinitialspace=True, delimiter = ',')
    userarray = list(userreader)

#These lines of code open the passwords csv file and read the items into an array called passarray
passwords = r'passwords.csv'
with open(passwords)as passfile:
    passreader = csv.reader(passfile, skipinitialspace=True, delimiter = ',')
    passarray = list(passreader)


#The UsernameValidator function checks a given username to see if it exists in userarray
#It then returns the position of the username in the array if found or says invalid username if not found
def UsernameValidator(userEnter):
    maxRange = (len(userarray[0]))
    for i in range(0, maxRange):
        if userEnter == userarray[0][i]:
            return (i)
        elif i == (maxRange - 1):
            return(-1)
        else:
            i += 1

#The PasswordValidator function checks to see if the given password is the same as the password stored at the same
# position in the array as the username
#If it matches, access is granted to the application, if not, it says invalid password
def PasswordValidator(passEnter, passPos):
    if passEnter == passarray[0][passPos]:
        return(1)
    else:
        return(-1)


"""
#These 2 print statements are testing that the files were read correctly
print(userarray)
print(passarray)

#These 2 temporary inputs took the place of an input box on the GUI
temp = input("What is your username? ")
temp2 = input("What is your password? ")

#Here the UsernameValidator function is called in the variable userPostion which will store the returned value
userPosition = UsernameValidator(temp)

#This if statement runs the PasswordValidator function if the username given was valid, if not, it doesn't run the function
if userPosition == -1:
    print()
else:
    checkAccess = PasswordValidator(temp2, userPosition)
"""

