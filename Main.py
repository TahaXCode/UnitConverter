import Length
import Weight
import Temperature
import Time
import Volume

choice = 0
while choice < 6:

    print("Please choose a converter type by entering the corresponding number:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Time")
    print("5. Volume")
    print("6. Exit")
    choice = int(input())

    if choice == 1:
        entry = float(input("Please enter a number:"))
        print("The following units are supported for conversion:")
        print("Length: meter (m), kilometer (km), mile, centimeter (cm)")

        unit = input("Please enter the unit you want to convert from (e.g., m, km, mile, cm): ").lower()
        unitconvert = input("Please enter the unit you want to convert to (e.g., m, km, mile, cm): ").lower()

        print(f"{unit} to {unitconvert} is: {Length.converter(entry, unit, unitconvert)}")

    elif choice == 2:
        entry = float(input("Please enter a number:"))
        print("The following units are supported for conversion:")
        print("Weight: kilogram (kg), gram (g), pound (lb), ounce (oz)")

        unit = input("Please enter the unit you want to convert from (e.g., kg, g, lb, oz): ").lower()
        unitconvert = input("Please enter the unit you want to convert to (e.g., kg, g, lb, oz): ").lower()

        print(f"{unit} to {unitconvert} is: {Weight.converter(entry, unit, unitconvert)}")

    elif choice == 3:
        entry = float(input("Please enter a number:"))
        print("The following units are supported for conversion:")
        print("Temperature: Celsius (C), Fahrenheit (F), Kelvin (K)")

        unit = input("Please enter the unit you want to convert from (e.g., C, F, K): ").upper()
        unitconvert = input("Please enter the unit you want to convert to (e.g., C, F, K): ").upper()

        print(f"{unit} to {unitconvert} is: {Temperature.converter(entry, unit, unitconvert)}")

    elif choice == 4:
        entry = float(input("Please enter a number:"))
        print("The following units are supported for conversion:")
        print("Time: seconds (s), minutes (min), hours (h)")

        unit = input("Please enter the unit you want to convert from (e.g., s, min, h): ").lower()
        unitconvert = input("Please enter the unit you want to convert to (e.g., s, min, h): ").lower()

        print(f"{unit} to {unitconvert} is: {Time.converter(entry, unit, unitconvert)}")

    elif choice == 5:
        entry = float(input("Please enter a number:"))
        print("The following units are supported for conversion:")
        print("Volume: liter (L), milliliter (mL), gallon (gal)")

        unit = input("Please enter the unit you want to convert from (e.g., L, mL, gal): ").lower()
        unitconvert = input("Please enter the unit you want to convert to (e.g., L, mL, gal): ").lower()

        print(f"{unit} to {unitconvert} is: {Volume.converter(entry, unit, unitconvert)}")

    elif choice == 6:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
