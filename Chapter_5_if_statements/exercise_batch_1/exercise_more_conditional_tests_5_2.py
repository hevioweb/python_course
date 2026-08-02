name = "Maria"
number = 20
list = list(range(1,10))
number_3 = 3
number_32 = 32

if name == "maria": # if name matches "" execute
    print("\nMatched")
if name != "maria": # if name does not match "" execute
    print("\nDoesnt match")

if name.lower() == "maria": 
    print("\nMatched with .lower() methode")
    
if number >= 18:
    print("\nnumber is greater")
    
if number <= 18:
    print("\nnumber is smaller")
    
if number >= 10 or number <= 10:
    print("\nor keyword")
    
if number >= 10 and number <= 10:
    print("\nand keyword keyword")

if number_3 in list:
    print("3 is in the list")
    
if number_32 not in list:
    print("32 is not in the list")
    
    