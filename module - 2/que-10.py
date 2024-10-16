#  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

num1 = int(input("enter num1 value :"))
num2 = int(input("enter num2 value :"))

if num1 == num2 or num1 + num2 == 5 or num1 - num2 == 5 :
    result = True
else :
    result = False
print("result :", result)        