numbers = list(range(1,20))
for number in numbers: 
    print(number)



numbers = list(range(1,1000000))
for number in numbers:
    print(number)



numbers = list(range(1,1000000))
print(min(numbers))
print(max(numbers))
print(sum(numbers))




numbers = list(range(1, 20, 3)) #it starts with 1 and adds 3 up until 19, it creates odd numbers
for number in numbers:
    print(number)



numbers = list(range(3,31))
for number in numbers:
    multiplier = number *3
    print(multiplier)
    
#list comprehensive 
numbers = [number *3 for number in range(3,31)]
for number in numbers:
    print(number)

 
 

cubes = [cube **3 for cube in range(1,11)]   
for cube in cubes:
    print(cubes)







