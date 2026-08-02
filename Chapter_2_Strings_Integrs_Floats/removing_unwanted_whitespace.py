# to remove unwonted white space we can use module .rstrip() for example

user_input = input("type something: ").rstrip()
print(f"No white spaces: \n\t{user_input}")