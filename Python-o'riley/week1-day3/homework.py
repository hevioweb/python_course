"""
Homework: Temperature & Unit Converter
_________________________________________
Concepts tested:
  - Defining functions with def, parameters, return values
  - Local vs Global scope
  - Importing custom modules with aliases
_________________________________________

Tasks:
  1. Import converter_module with alias cv.
     Create a global variable WELCOME = "Unit Converter Ready!".

  2. Write a function convert_temps(temp_list, target_unit) that
     converts a list of Celsius temps to Fahrenheit ("F") or back ("C").
     Use a local list variable inside the function and return it.

  3. Write a main() function that:
     - Prints the global WELCOME
     - Calls convert_temps([0, 25, 100], "F") and prints the result
     - Calls convert_temps([32, 72, 212], "C") and prints the result
     - Converts 10 km to miles using cv.km_to_miles() and prints it

Run this file to verify everything works.
"""

# === YOUR CODE BELOW ===

#task 1

import converter_module as cv
WELCOME = "Unit Converter Ready!"

#task 2

def convert_temps(temp_list, target_unit):
    converted_temps = []
    for temp in temp_list:
        if target_unit == "F":
            converted_temp = cv.celsius_to_fahrenheit(temp)
        elif target_unit == "C":
            converted_temp = cv.fahrenheit_to_celsius(temp)
        converted_temps.append(converted_temp)
    return converted_temps

#task 3

def main():
    print(WELCOME)
    print(convert_temps([0, 25, 100], "F"))
    print(convert_temps([32, 72, 212], "C"))
    print(cv.km_to_miles(10))

main()