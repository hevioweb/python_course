# write a programm that removes all unwanted characters from a string and returns the cleaned string.

import re

def clean_text(text):
   
    #remove all non-alphanumeric characters (except spaces)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text) #r'[^a-zA-Z0-9 ]' means find all characters that are not letters, digits, or spaces and replace them with an empty string
    
    #remove extra spaces
    text = " ".join(text.split())  #text.split() splits the text into a list of words, and " ".join() joins them back into a string with a single space between each word
    return text.lower()  #convert to lowercase



input_text = "Hello, World! This is a test.   "
cleaned = clean_text(input_text)
print(cleaned)  # Output: "hello world this is a test"
    