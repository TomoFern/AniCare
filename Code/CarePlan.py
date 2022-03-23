import csv

breeds = r'C:\Users\stu-fernandez.t.HUNGERHILL\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\AniCare\Code\animals.csv'
with open(breeds) as breedsfile:
    breedsreader = csv.reader(breedsfile)
    breedsarray = list(breedsreader)

print(breedsarray)

#animalAge = input("How old is the animal: ")
animalBreed = input("What breed is the animal: ")
#animalWeight = input("How much does the animal weigh: ")
#animalSex = input("What is the sex of the animal: ")
#animalName = input("What is the name of the animal: ")

def AnimalLocator(breed):
    breedFound = False
    i = 1
    while breedFound == False:
        if breedsarray[i][0] == breed:
            print("found")
            breedFound = True
        elif i == len(breedsarray) - 1:
            print("not found")
            break
        else:
            i += 1

AnimalLocator(animalBreed)

