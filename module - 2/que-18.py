#  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged. 

string1 = input("enter string (length should be at least 3) :")
string2 = "ing"

if len(string1) >= 3 :
    if string1.endswith("ing"):
        result = string1 + "ly"
    else :
        result = string1 + "ing"
else:
    print("enter length should be at least 3")
print(result)    
