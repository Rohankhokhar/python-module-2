#  Write a Python program to count the occurrences of each word in a given sentence 

string = input("enter a string :")

words = string.split()

word_count = {}

for word in words :
    if word in word_count :
        word_count[word]  += 1
    else :
        word_count[word] = 1

for word , word_count in word_count.items() :
    print(f"word :{word} = {word_count}")

