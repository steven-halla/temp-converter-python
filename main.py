################################################################
# Project: Temperture converter
# File: main.py
# Description: This program will conver celisus to farenhegith and vice versa
                # this program includes validatiosn for user input
                #uses a WHile loop with if statemnts.
# Author: Steven Halla
# Version: 1.0
# Date: April 28th 2023
################################################################

from typing import Union

from typing import Union


def convert_temperature() -> None:
    running: bool = True

    while running:
        print("Press 1: Fahrenheit to Celsius. Press 2: Celsius to Fahrenheit")
        try:
            userInput: int = int(input("Enter your choice: "))
        except ValueError:
            print("Please input a number only")
            continue

        if userInput > 2 or userInput < 1:
            print("Please input 1 or 2 only")
        elif userInput == 1:
            print("Fahrenheit to Celsius conversion")
            try:
                fahrenheit: float = float(
                    input("Enter temperature in Fahrenheit: "))
            except ValueError:
                print("Please input a number only")
                continue
            celsius: float = (fahrenheit - 32) * 5 / 9
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
        elif userInput == 2:
            print("Celsius to Fahrenheit conversion")
            try:
                celsius: float = float(input("Enter temperature in Celsius: "))
            except ValueError:
                print("Please input a number only")
                continue
            fahrenheit: float = (celsius * 9 / 5) + 32
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        else:
            print("Please input 1 or 2 only")

        while True:
            choice: str = input("Do you want to continue? (y/n)").lower()
            if choice == "n":
                running = False
                print("Exiting program...")
                break
            elif choice == "y":
                break
            else:
                print("Please enter 'y' or 'n' only.")


if __name__ == "__main__":
    convert_temperature()
