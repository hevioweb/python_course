import re

# Concatenation of strings
first = "hello"
second = "world"
result = first + " " + second
print(result)


# Slice of strings
text = "Python programming"
print(text[0:6])  # Python
print(text[7:18])  # programming


# Formating strings
name = "Alice"
age = 25
message = f"Hello, my name is {name} and I am {age} years old."
print(message)


# Common string methods

#split()
sentence = "This is a sample sentence."
words = sentence.split()
print(words)

#join()
new_sentence = " ".join(words)
print(new_sentence)

#replace()
text = "I like apples."
new_text = text.replace("apples", "oranges")
print(new_text)

#strip()
messy = "                Hello, World!           "
clean = messy.strip()
print(clean)





# Regular expressions dor Pattern Matching

import re

text = "Contact me at 123-456-7890"
digits = re.findall(r'\d+', text) #r'\d+' means find all sequences of digits
print(digits)  # Output: ['123', '456', '7890']

update_text = re.sub(r'\d', 'X', text)  #r'\d' means find all digits and replace with 'X'
print(update_text)  # Output: Contact me at XXX-XXX-XXXX