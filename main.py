import os
import json
import datetime
from os.path import exists

# Defining variables.
location = ""
maxPosition = 2863.00
curPosition = 0.00

def determineLocation(position) -> str:
    # Setting a local variable to avoid errors.
    location = ""

    # Determining the players position based on distance travelled.
    if position >= maxPosition:
        location = "Mount Doom"
    elif position >= 2106:
        location = "Rauros Falls"
    elif position >= 1480:
        location = "Lothlorien"
    elif position >= 737.08:
        location = "Rivendell"
    elif position >= 193.12:
        location = "Bree"
    elif position >= 10:
        location = "Old Forest"
    elif position >= 0:
        location = "The Shire"

    return location

def loadProgress():
    if exists("progress.txt"):
        f = open("progress.txt", "r")
        data = json.loads(f.read())

        global curPosition
        curPosition = data['basic']["curPosition"]

        global location
        location = determineLocation(curPosition)
    else:
        # Creating variables for loading later.
        date = datetime.datetime.now()
        contents = {'basic': {"startDate": str(date), "endDate": "", "curPosition": 0.00}}

        json_object = json.dumps(contents)
        f = open("progress.txt", "w")
        f.write(json_object)
        f.close()

        loadProgress()

loadProgress()

def addProgress():
    if exists("progress.txt"):
        f = open("progress.txt", "r")
        data = json.loads(f.read())
        f.close()

        distance = float(input("Enter distance."))
        data['basic']["curPosition"] = data['basic']["curPosition"] + distance
        json_object = json.dumps(data)

        f = open("progress.txt", "w")
        f.write(json_object)
        f.close()

        loadProgress()

def menu():
    percentage = round(((curPosition/maxPosition)*100), 2)
    print("====================================")
    print("Current Location: " + location)
    print("Distance Travelled: " + str(curPosition) + "km (" + str(percentage) + "%)")
    print("Distance Left: " + str((maxPosition - curPosition)) + "km (" + str((100-percentage)) + "%)")
    print("====================================")

    print("1. Add progress")
    print("2. Statistics")
    print("3. Settings")
    print("0. Exit")

menu()
option = int(input("Enter selection."))

while option != 0:
    if option == 1:
        addProgress()
    elif option == 2:
        print("2")
    else:
        print("Not valid input.")
    menu()
    option = int(input("Enter selection."))
