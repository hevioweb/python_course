#function syntax (define a function)

# def function_name(parameters):
#     #Code block
#     return result




#function with parameters and return value

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result) # Output: 8




#local scope

def greet(): #function is created
    name = "Alice"  # This variable is local to the greet function
    print(name)
    
greet()  # function is called, it will print "Alice"
# print(name)  # This will cause an error because name is not defined outside the greet function




#Global scope

greeting = "Hello, world!"

def say_hello():
    print(greeting)  # This will access the global variable greeting

say_hello()  # Output: Hello, world!




#Importing entire modules

import math
print(math.sqrt(16))  # Output: 4.0




#Importing specific functions

from math import sqrt
print(sqrt(25))  # Output: 5.0




#Importing with an alias (shorter name)

import math as m
print(m.sqrt(36))  # Output: 6.0