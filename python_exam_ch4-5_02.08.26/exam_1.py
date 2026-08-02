# =====================================================================
# EXAM 1 - Chapter 4 (Working with lists) & Chapter 5 (if statements)
# Date: 02.08.26
#
# RULES:
#   - Only use what you learned in chapters 1-5.
#   - Not allowed: input(), while loops, dictionaries, def, classes,
#     files, try/except, imports.
#   - Write your answer under each task, where it says "your code here".
#   - Run the file often to check your output.
# =====================================================================



# ---------------------------------------------------------------------
# TASK 1 - Counting (for loops + range)
#
# Make a list called numbers that holds the numbers 1 to 20 by using
# list() together with range().
# Then use a for loop to print every number on its own line.
# ---------------------------------------------------------------------

numbers = list(range(1,21))

for number in numbers:
   print(number)

# ---------------------------------------------------------------------
# TASK 2 - Every fifth number (third argument of range)
#
# Make a list called fives that holds 5, 10, 15 ... up to 50, by using
# the third argument of range().
# Print the list, then print the smallest number, the biggest number
# and the sum of all the numbers.
# Use f-strings so the output looks like:
#   The smallest number is: 5
# ---------------------------------------------------------------------

fives = list(range(5, 51, 5))

print(fives)
print(f"the sum of all numbers is: {sum(fives)}")
print(f"the min of all numbers is: {min(fives)}")
print(f"the max of all numbers is: {max(fives)}")



# ---------------------------------------------------------------------
# TASK 3 - List comprehension
#
# Make a list called squares that holds the numbers 1 to 10 multiplied
# by themselves (1, 4, 9, 16 ...). You MUST do it in one line with a
# list comprehension.
# Then print each item of squares with a for loop.
# ---------------------------------------------------------------------

squares = [square **2 for square in range(1,11)]
for square in squares:
    print(square)

# ---------------------------------------------------------------------
# TASK 4 - Slicing
#
# Make a list called foods with exactly 6 different foods.
# Then print:
#   - the first three foods
#   - the three foods from the middle of the list
#   - the last three foods
# Before each one print a small title line, for example:
#   The first three foods are:
# ---------------------------------------------------------------------

foods = ["Food_1", "Food_2", "Food_3", "Food_4", "Food_5", "Food_6",]

print(f"\nThe first 3 food are: {foods[:3]}")
print(f"\nThe middle 3 food are: {foods[2:4]}")
print(f"\nThe last 3 food are: {foods[3:]}\n")


# ---------------------------------------------------------------------
# TASK 5 - Copying a list
#
# Copy the list foods from task 4 into a new list called friend_foods.
# (Remember: copying a list is done with a slice without indexes.)
# Add one new food to foods, and a DIFFERENT new food to friend_foods.
# Print both lists to prove that they are two separate lists.
# ---------------------------------------------------------------------

foods_2 = ["Food_1", "Food_2", "Food_3", "Food_4", "Food_5", "Food_6",]
new_foods = foods_2[:]

foods_2.append("Food_7")
new_foods.insert(0, "New Food")

print(new_foods)
print(foods_2)


# ---------------------------------------------------------------------
# TASK 6 - Tuples
#
# Make a tuple called gym_gear with 4 pieces of gym equipment.
# Print every item of the tuple with a for loop.
# Then redefine the whole tuple (2 items stay the same, 2 items change)
# and print all the items again with a for loop.
# ---------------------------------------------------------------------

gym_gear = ("dumbell", "gear", "benchpress", "weight")

for gear in gym_gear:
    print(f"{gear} is our gym gear")
    
gym_gear = ("dumbell", "press", "smith machien", "weight")

for gear in gym_gear:
    print(f"{gear} is our gym gear")
    


# ---------------------------------------------------------------------
# TASK 7 - if-elif-else chain
#
# Make a variable called temperature and give it a number.
# Then write an if-elif-else chain that prints:
#   temperature 0 or lower   -> "It is freezing, stay home"
#   temperature 1 to 10      -> "It is cold, take a jacket"
#   temperature 11 to 20     -> "It is fresh outside"
#   temperature 21 to 30     -> "It is warm, nice day"
#   anything higher          -> "It is too hot, drink water"
# Test your chain by changing the value of temperature a few times.
# ---------------------------------------------------------------------

temp = 0

if temp <= 0:
    print("It is freezing, stay home")
elif temp <= 10:
    print("It is cold, take a jacket")
elif temp <= 20:
    print("It is fresh outside")
elif temp <= 30:
    print("It is warm, nice day")
else:
    print("It is too hot, drink water")


# ---------------------------------------------------------------------
# TASK 8 - if statements inside a loop (in / not in)
#
# Make a list called current_users with 5 usernames (mix upper and
# lowercase letters).
# Make a list called new_users with 5 usernames, where 2 of them are the
# same as in current_users but written with different capitalization.
#
# Make lowercase copies of both lists using list comprehensions.
# Then loop over the new users and print for each one:
#   - if the name is already taken: "<name>, this username is taken"
#   - if it is free:                "<name>, your username is accepted"
# ---------------------------------------------------------------------

current_users = ["joD", "dawW", "piI", "Oik", "kif"]
new_users = ["Dih", "dawW", "uiD", "Oik", "rolAnd"]

current_users_lower = [current_users.lower() for current_users in current_users]
new_users_lower = [new_users.lower() for new_users in new_users]

for user in new_users_lower:
    if user in current_users_lower:
        print(f"\n\t{user}, username already in use")
    else:
        print(f"\n{user}, your username is accepted")
        

# ---------------------------------------------------------------------
# TASK 9 - Empty list check
#
# Make an empty list called waiting_line.
# If the list has names in it, loop over it and greet every person.
# If the list is empty, print "Nobody is waiting right now".
# After that, add 3 names to waiting_line and run the same kind of check
# again, so this time the people get greeted.
# ---------------------------------------------------------------------

waiting_line = ["person_0", "person_1", "person_3",]

if not waiting_line:
    print("\nNobody is waiting right now")
else:
    print(f"\nCurently {len(waiting_line)} people in line")
    for person in waiting_line:
        print(f"Welcome, {person}")


# ---------------------------------------------------------------------
# BONUS TASK - and / or
#
# Make two variables: age and ticket ("yes" or "no").
# Write one if statement that uses the "and" keyword: the person may
# enter only if age is 18 or higher AND ticket is "yes".
# Write a second if statement that uses the "or" keyword: print a
# discount message if age is under 12 OR age is 65 and higher.
# Add an else to each one so something is printed in every case.
# ---------------------------------------------------------------------

age = 11
ticket = True
rich_daddys_boy = True

if age >= 18 and ticket == True:
    print("\nYou can come in")
elif rich_daddys_boy == True:
    print("\nAlr this one time")
else:
    print("\nHell nah, get outta here")
    
if age <= 12 or age >= 65 and ticket == True:
    print("\nYou may receave a discount")
else:
    print("\nNo discount")
    

# =====================================================================
# END OF EXAM - good luck!
# =====================================================================
