print("choose waht you want to convert: \n1. Celsius to Fahrenheit \n2. Kilometers to Miles \n3. Kilograms to Pounds")
user_input = float(input("Enter your choice (1-3): "))
user_value = float(input("Enter the value you want to convert: "))

def celsius_to_fahrenheit(celsius):
    user_value = celsius * 9/5 + 32
    return user_value

def kilometers_to_miles(kilometers):
    user_value = kilometers * 0.621371
    return user_value

def kilograms_to_pounds(kilograms):
    user_value = kilograms * 2.20462
    return user_value

if user_input == 1:
    celsius_to_fahrenheit(user_value)
    print(f"{user_value} Celsius is equal to {celsius_to_fahrenheit(user_value)} Fahrenheit")
elif user_input == 2:
    kilometers_to_miles(user_value)
    print(f"{user_value} Kilometers is equal to {kilometers_to_miles(user_value)} Miles")
elif user_input == 3:
    kilograms_to_pounds(user_value)
    print(f"{user_value} Kilograms is equal to {kilometers_to_miles(user_value)} pounds")