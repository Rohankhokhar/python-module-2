#  Write a Python function to reverses a string if its length is a multiple of 4

def resstr(string):
    if len(string) % 4 == 0:
        return string[::-1]
    

string1 = input("enter a string:")   
res = resstr(string1) 

print(res)