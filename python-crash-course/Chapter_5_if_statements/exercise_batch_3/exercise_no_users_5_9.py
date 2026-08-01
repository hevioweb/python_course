users_list = []

if users_list:
    for users_list in users_list: #if we want to make a program like this we must use same variable in the for loop twice: for var in var
        if users_list == "admin":
            print("\nHello Admin, would you like a status report\n")
        else:
            print(f"Welcome, back {users_list}") 
else:
    print("We need users") #if no conditions before execetus the else statement is executed
        
