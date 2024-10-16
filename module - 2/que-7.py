# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

num = int(input("enter a number value to check odd or even :"))

if num % 2 == 0:
    print("number is even ")
elif num % 2 != 0:
    print("number is odd ")
else :
    print("number is zero ")    


