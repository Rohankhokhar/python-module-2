#  Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

ch = input("enter a string :")

if len(ch) < 2 :
    print("")
else :
    print(ch[:2]+ch[-2:])    


 