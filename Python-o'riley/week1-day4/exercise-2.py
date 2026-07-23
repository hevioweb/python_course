# storing user input in a dictionary

sentence = input("Enter a Sentence: ")

# split the sentence into words
words = sentence.split()

# init Dictionary
word_count = {}

# Count word Frequence
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else: 
        word_count[word] = 1
        
print(word_count)

