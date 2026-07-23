# Homework — Week 1 Day 2
# Solve each task below. Write your code under each comment.



# Task 1: Nested conditions
# Create a variable age = 20 and has_id = True.
# If age >= 18, check if has_id is True — then print "Allowed in".
# Otherwise print "Need ID". If age < 18, print "Too young".

age = int(input("Enter your age: "))
has_id = int(input("do you have ID? (1 for yes, 0 for no): "))

if age >= 18:   # use >= because if its just > then 18 year olds would not be allowed in
    if has_id == 1:
        print("Allowed in")
    else:
        print("Need ID")
else:
    print("Too young")



# Task 2: For loop + Break
# Loop through numbers 1 to 20. If the number is 13, print "Unlucky!"
# and break. Otherwise print the number.
for i in range(1, 21): # if 1, 20 the loop will go only until 19, we need to use 21 to include 20 in the loop
    if i == 13:
        print("Unluck")
        break
    else:
        print(i, "you are lucky")
  





# Task 3: While loop + Continue
# Start count = 0. While count < 10, increment count by 1 each loop.
# Use continue to skip printing odd numbers (hint: count % 2 == 0).
# Print only the even numbers.

count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        print(count, "is even")
    else:
        continue