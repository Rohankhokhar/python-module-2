#  Write a Python program to count the number of characters (character frequency) in a string

string = input("enter string :")

c = {}

for char in string :
    if char in c :
        c[char] += 1
    else :
        c[char] = 1
print("Character frequency:")
for char, c in c.items():
    print(f"'{char}': {c}")        

