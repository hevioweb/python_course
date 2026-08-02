curent_users = ["maila", "jOhn", "pit32", "marv", "maxutka", "benni"]
new_users = ["maya", "jOHn", "uyp", "MARV", "mika", "suba"]

# copy a list and convert all the values to lowercase
curent_users_lower = [curent_users.lower() for curent_users in curent_users]  # using comprehensive lists
new_users_lower = [new_users.lower() for new_users in new_users]  # using comprehensive lists

for new_user in new_users_lower: 
    if new_user in curent_users_lower:
        print(f"\n\t{new_user}, that username is already taken")
    else:
        print(f"\n{new_user}, your user name is accepted")


# in the loop for example: for new_user in new_users_lower: 
# the variable before in is the loop variable which is used to execute the code in the loop 
# and the variable after in is the list (existing variable)
