# Example 1: checking a condition
num = 4
nword = "nigga"
if num > 5:
    print("The number is ", num)
elif num == 5:
    print("The number is 5")
else: 
    print(nword)
    
    
    
# Example 2: Nested conditions
age = 25
if age > 18:
    if age < 30:
        print("You are a young adult.")
    else:
        print("You are an adult.")
    
    
        
# Example 3: For Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
for i in range(5): # 0,1,2,3,4
    print(i)
    
    
    
# Example 4: While Loop countdown
count = 5
while count > 0:
    print(count)
    count -= 1 
print("Liftoff!")



# Example 5: Break
for i in range(10):
    if i == 5:
        break  #basicly stops the loop when i is 5
    print(i)
    


# Example 6: Continue
for i in range(10):
        if i == 5:
          continue  #basicly skips the number in if
        print(i)