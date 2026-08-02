# last lesson we cover \n
# lets use \t to create tabs but we can also combine it with \n for exampel

# items = ("Items: \n\tPen\n\truler\n\tbox")
# print(items.title())


# to remove unwonted white space we can use module .rstrip() for example

# user_input = input("type something: ").rstrip()
# print(f"No white spaces: \n\t{user_input}")


# removing prefixes for example from urls https://

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

# or to permentaly remvoe the prefixes we can assign the methode to new variable

nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)