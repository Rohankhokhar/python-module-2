#  Write a Python function to insert a string in the middle of a string.

def insert(main,sub):
    midi = len(main)//2
    new_str = main[:midi] + sub + main[midi:]
    return new_str
mainstr = "hello world good morning"
substr = "fine to all"

res = insert(mainstr,substr)
print(res)