# write and read a list of items


#function for writing items to a file (overwrites existing content)

def write_items_to_file(filename, items): # items is a list of items we want to write
    with open(filename, "w") as file:
        for item in items:   # for each item in the collection
            file.write(item + "\n")  # this writes the item followed by a newline character



            
#function for ading things to alrerady existing file and its content

def append_items_to_file(filename, items):
    with open(filename, "a") as file:  # "a" mode is for appending to the file
        for item in items:
            file.write(item + "\n")           
            
            
            
                        
#function for reading items from a file

def read_items_from_file(filename):
    try:
        with open(filename, "r") as file:
            items = file.readlines()  # readlines() reads amount of lines in a file 
            print("Items in the file:")
            for item in items:
                print(item.strip()) #print each item without the newline character
    
    except FileNotFoundError:
        print(f"File {filename} not found.")
        



fruits = ["cherry", "ananas", "pineapple", "grape", "watermelon"] #list of items we want to wite/append to the file

append_items_to_file("fruits.txt", fruits) #fruits.txt is the name of the file  |  fruits is the list of items we want to write
# write_items_to_file("fruits.txt", fruits)             #for now disabled to let the function above to execute
read_items_from_file("fruits.txt")