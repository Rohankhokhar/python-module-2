# Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.

string1 = input("enter a string 1 :")
string2 = input("enter a string 2 :")

stringn1 = string2[: 2] + string1[2 :]
stringn2 = string1[: 2] + string2[2 :]

print(stringn1 + " " + stringn2)