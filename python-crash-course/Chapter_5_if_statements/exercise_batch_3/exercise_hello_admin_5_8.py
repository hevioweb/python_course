users_list = ["maila", "jOhn", "pit32", "marv", "maxutka", "admin"]

for user in users_list: #if we want to make a program like this we must use same variable in the for loop twice: for var in var
    if user == "admin":
        print("\nHello Admin, would you like a status report\n")
    else:
        print(f"Welcome, back {user}") 
        
