my_pizza = ['pepperoni', 'mushroom', 'green pepper']

friends_pizza = my_pizza[:]

my_pizza.append("salami")
friends_pizza.insert(0, "pizza")


print("\nMy favourite pizzas are:")
for pizza in my_pizza:
    print(pizza)
    
print("\nFirends favourite pizzas are:")
for pizza in friends_pizza:
    print(pizza)