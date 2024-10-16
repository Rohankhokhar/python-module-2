#  Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 
str = input("Enter a string: ")

find1 = str.find("not")
find2 = str.find("poor")
    
if find1 != -1 and find2 != -1 and find1 < find2:
    result = str[:find1] + 'good' + str[find2 + 4:]
else:
    result = str

print("string:", result)

print("----------------------------------------")

str = input("Enter a string: ")

if "not" in str and "poor" in str :
    find1 = str.find("not")
    find2 = str.find("poor")
    
    if  find1 < find2:
       result = str[:find1] + 'good' + str[find2 + 4:]
    else:
       result = str

print("string:", result)




