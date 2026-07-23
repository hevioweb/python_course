#file opening example
with open("info.txt","r") as file:   # file is automatically closed (using "with" statement)
    content = file.read()
    print(content)
    
    
#file writing example
with open("info.txt","w") as file:   # file is automatically closed (using "with" statement)
    file.write("This is a new line of text.")
    file.writelines(["bob", "slice", "example"])
    
    
#using try-except to handle file not found error
try:
    with open("nonexistent.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")