#  Write a Python function that takes a list of words and returns the length 
# of the longest one. 

def long(list1):
    big = 0
    for i in list1:
        if len(i) > big:
            big = len(i)
    return big

string = "python is easy languge"
words = string.split()
res = long(words)
print(res)        