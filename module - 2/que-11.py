#  Write a python program to sum of the first n positive integers

n = int(input("enter a range of n number integer :"))
sum = 0

for i in range(1 , n+1) :
    sum += i
print("result of n number int sum is :" , sum)    