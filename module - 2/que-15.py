#  Write a Python program to count occurrences of a substring in a string. 

main_string = input("enter main string:")
sub_string = input("enter sub string :")

count = main_string.count(sub_string)

print(f"sub string in {sub_string} in count {count} times in main string")