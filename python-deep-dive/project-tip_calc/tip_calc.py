# while True:
#    try:
#        bill = float(input("Enter amount of what the user spent: "))
#        tip_precentage = float(input("Enter how much a user tipped: "))
#        tip_amount = bill * tip_precentage / 100
#        total = bill + tip_amount
#        print(f"User has to pay: {total:.2f}")
#        break
#    except ValueError:
#     print("Please enter a valid number")
     
     
#     # for improving try to restructer everything intofunctions like one that takes results one that calculates and one that give the answears back





def calculation():   
    bill = float(input("Enter amount of what the user spent: "))
    tip_precentage = float(input("Enter how much a user tipped: "))
    total = bill + bill * tip_precentage / 100
    return total
    

while True:
    try:
        total = calculation()
        print(f"User has to pay: {total:.2f}")
        break
    except ValueError:
        print("Please enter a valid number")
        


