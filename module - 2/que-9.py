# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num1 = int(input("enter a num1 value :"))
num2 = int(input("enter a num2 value :"))
num3 = int(input("enter a num3 value :"))

if num1 == num2 or num1 == num3 or num2 == num3 :
    sum = 0
else :
    sum = num1 + num2 + num3  

print("result of 3 number sum :" ,sum)  