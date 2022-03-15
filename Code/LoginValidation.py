#Imports the csv library allowing me to open and read and write to a csv file
import csv

usernames = r"c:\Users\stu-fernandez.t\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\AniCare\Code\usernames.csv"
with open(usernames)as userfile:
    userreader = csv.reader(userfile, skipinitialspace=True, delimiter = ',')
    userarray = list(userreader)

passwords = r"c:\Users\stu-fernandez.t\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\AniCare\Code\passwords.csv"
with open(passwords)as passfile:
    passreader = csv.reader(passfile, skipinitialspace=True, delimiter = ',')
    passarray = list(passreader)

print(userfile)
print(userarray)
print(passarray)


def UsernameValidator(userEnter):
    maxRange = (len(userarray[0]))
    for i in range(0, maxRange):
        if userEnter == userarray[0][i]:
            print("test")
            return (i)
        elif i == (maxRange - 1):
            return("Invalid Username")
        else:
            i += 1

def PasswordValidator(passEnter, passPos):
    if passEnter == passarray[0][passPos]:
        print("Valid Password")
        return(1)
    else:
        print("Invalid Password")
        return(-1)

temp = input("What is your username? ")
temp2 = input("What is your password? ")

userPosition = UsernameValidator(temp)

if userPosition == "Invalid Username":
    print(userPosition)
else:
    checkAccess = PasswordValidator(temp2, userPosition)

