#lists 

numbers = [1, 2, 3, 4]

fruits = ["apples", "banana", "cherry"]

print(fruits[0])
print(numbers[2])
print(numbers[-1])

# list modifyers

numbers.append(5)
fruits.insert(1, "annanas")
fruits.remove("apples")
del fruits[0]
fruits.pop

# slicing lists

sliced_fruits = fruits [0:2]
print(sliced_fruits)






#Tuples 

colors = ("red" , "green", "Blue",)
single_item = ("glass",)  #if you want single ellement tupple you need to put ,  at the end  otherwise its just a string






#Dictionary

student = {"name": "alice", "age": 25, "grade": 2,}
print(student["age"])

#modefying & acessing
student["subject"] = "math"
student["age"] = 32

print(student)

del student["grade"]
student.pop("subject")

#iteration 

for key, value in student.items():
    print(key, value)






#sets

number = {1, 2}
empty_set = set()

#adding and removing ellements

print(number)
number.add(5)
print(number)
number.remove(2)
print(number)

#set opperations

set1 = {1, 2, 3}
set2 = {3, 4, 5}

 #union

print(set1 | set2) # it unions the two sets but removes one 3 because it´s a dublicat 

 #intersection

print(set1 & set2) # only getting the intersection point like 3

 #diffrence
 
print(set1 - set2) # diffrence between set1 and set2 