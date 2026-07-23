# Cheack if a string is a palindrome (reads the same backward as forward)

def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum()) #text = "".join(char.lower() for char in text if char.isalnum()) removes all non-alphanumeric characters and converts the text to lowercase
    return text == text[::-1]  # check if the cleaned text is the same as its reverse

input_text = input("Enter a string: ")
if is_palindrome(input_text):
    print(f"'{input_text}' is a palindrome.")
else:
    print(f"'{input_text}' is not a palindrome.")