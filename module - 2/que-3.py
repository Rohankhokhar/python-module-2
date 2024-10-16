# Write a Python program to get the Fibonacci series of given range. 

n = int(input("enter Fibonacci series range value : "))

a = int(input("enter first Fibonacci series 1st value : "))
b = int(input("enter first Fibonacci series 2nd value : "))

print(a , b , end=" ")

for f in range (3,n+1):
    c = a + b
    print(c , end = " ")     
    a = b
    b = c
