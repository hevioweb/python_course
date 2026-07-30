my_foods = ["pizza", "falafel", "cake"]
friends_foods = my_foods[:]

my_foods.append("food1")
friends_foods.insert(0, "food2")

print("\nMy favourite foods are:")
for food in my_foods:
    print(food.title())
    
print("\nMy firends favourite foods are:")
for food in friends_foods:
    print(food.title())
    