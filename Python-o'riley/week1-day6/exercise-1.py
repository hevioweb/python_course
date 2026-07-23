# Count Words and lines in a file
def count_words_and_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines() #list of lines in the file
            lines_count = len(lines) #count the number of lines   len() function counts the number of items in a list
            words_count = sum(len(line.split()) for line in lines) #count the number of words   split() function splits a string into a list of words   sum() function sums up the counts of words in each line
            
            print(f"Number of lines: {lines_count}")
            print(f"Number of words: {words_count}")
    except FileNotFoundError:
        print("Fuck you.")
         


count_words_and_lines("info.txt")         