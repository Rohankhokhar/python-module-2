#  Write python program that swap two number with temp variable and without temp variable. 

num1 = 10
num2 = 20

temp = num1
num1 = num2
num2 = temp

print("num1 :",num1 , "num2 :",num2)

num1 , num2 = num2 , num1

print("swaping without temp varible : num1 :" , num1 , "num2 :",num2)