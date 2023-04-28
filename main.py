################################################################
# Project: Temperture converter
# File: main.py
# Description: This program will conver celisus to farenhegith and vice versa
# Author: Steven Halla
# Version: 1.0
# Date: April 28th 2023
################################################################

running = True

while running:
    #user gets 2 choices
    print("Press 1: Fahrenheit to Celsius. Press 2: Celsius to Fahrenheit")
    userInput = int(input("Enter your choice: "))

    #error handling for wrong input
    if userInput > 2 or userInput < 1:
        print("Please input 1 or 2 only")

        #lets user convert fahrenheit to celcius
    elif userInput == 1:
        print("Fahrenheit to Celsius conversion")
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
        #lets user conver celcius to fahrenheit
    elif userInput == 2:
        print("Celsius to Fahrenheit conversion")
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
    else:
        print("Please input 1 or 2 only")

    # ask the user if they want to continue
    while True:
        choice = input("Do you want to continue? (y/n)").lower()
        if choice == "n":
            running = False
            print("Exiting program...")
            break
        elif choice == "y":
            break
        else:
            print("Please enter 'y' or 'n' only.")





