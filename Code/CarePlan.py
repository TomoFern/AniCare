from ast import And
import csv

# breeds = r'C:\Users\stu-fernandez.t\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\AniCare\Code\animals.csv'
breeds = r'Code\animals.csv'
with open(breeds) as breedsfile:
    breedsreader = csv.reader(breedsfile)
    breedsarray = list(breedsreader)

print(breedsarray)

#animalAge = input("How old is the animal: ")
animalBreed = input("What breed is the animal: ")
animalWeight = input("How much does the animal weigh: ")
animalSex = input("What is the sex of the animal: ")
animalName = input("What is the name of the animal: ")

def AnimalLocator(breed):
    breedFound = False
    n = 1
    while breedFound == False:
        if breed == "":
            print("Must input a breed!")
            break
        elif breedsarray[n][0] == breed:
            print("found")
            breedFound = True
            return (n)
        elif n == len(breedsarray) - 1:
            print("not found")
            break
        else:
            n += 1

def WeightChecker(sex, breed, weight):
    fom = 0
    if sex == "":
        print("Must input a sex!")
    elif sex == "Male":
        fom = 1
    elif sex == "Female":
        fom = 4
    else:
        print("Not a valid sex, please enter Male or Female")
    
    minWeight = breedsarray[int(breed)][int(fom)]
    maxWeight = breedsarray[int(breed)][int(fom + 1)]
    meanWeight = breedsarray[int(breed)][int(fom + 2)]

    print("minimum", minWeight)
    print("maximum", maxWeight)
    print("mean", meanWeight)

    if weight < maxWeight and weight > minWeight:
        print ("Your dog is a healthy weight")
        if weight < meanWeight:
            difference = (float(meanWeight) - int(weight))
        elif weight > meanWeight:
            difference = (int(weight) - float(meanWeight))
        roundedDifference = round(difference, 3)
        print (roundedDifference)
    elif weight > maxWeight:
        over = (int(weight) - float(maxWeight))
        roundedOver = round(over, 3)
        print("Your dog is", roundedOver, "kg overweight")
    elif weight < minWeight:
        under = (float(minWeight) - int(weight))
        roundedUnder = round(under, 3)
        print("Your dog is", roundedUnder, "kg underweight")

def checklistGenerator(name):
    print("")

breedLocation = (AnimalLocator(animalBreed))

WeightChecker(animalSex, breedLocation, animalWeight)


