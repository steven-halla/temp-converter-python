# Steven Halla
# Intro to programming Python
#temp converter function WITH return

from typing import Optional


def temperature_converter() -> Optional[float]:
    running: bool = True
    results: list[Optional[float]] = []
    # while loop so we can allow the user to keep running the program if they want
    # to run both conversions
    while running:
        print("Press 1: Fahrenheit to Celsius. Press 2: Celsius to Fahrenheit")
        try:
            user_input: int = int(input("Enter your choice: "))
        except ValueError:
            print("Please input a number only")
            continue

        if user_input > 2 or user_input < 1:
            print("Please input 1 or 2 only")
            # Fahrenheit to Celsius
        elif user_input == 1:
            print("Fahrenheit to Celsius conversion")
            try:
                fahrenheit: float = float(
                    input("Enter temperature in Fahrenheit: "))
            except ValueError:
                print("Please input a number only")
                continue
            celsius: float = (fahrenheit - 32) * 5 / 9
            results.append(celsius)
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
        # Celsius to Fahrenheit
        elif user_input == 2:
            print("Celsius to Fahrenheit conversion")
            try:
                celsius: float = float(input("Enter temperature in Celsius: "))
            except ValueError:
                print("Please input a number only")
                continue
            fahrenheit: float = (celsius * 9 / 5) + 32
            results.append(fahrenheit)
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        else:
            print("Please input 1 or 2 only")

        # exit program or keep going
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

    if results:
        return results[-1]
    else:
        return None


def main() -> None:
    result = temperature_converter()
    if result is not None:
        print(f"The last converted temperature was: {result}")


if __name__ == "__main__":
    main()
