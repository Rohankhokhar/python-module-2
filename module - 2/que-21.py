#Write a Python function that takes a list of words and returns the length of the longest one.

ch = input("enter a string :")

words = ch.split()
big_words = (words[0])

for word in words : 
    if len(word) > len(big_words) :
        big_words = word
print("biggest word of string is :",big_words)        



