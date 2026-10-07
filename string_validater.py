'''Task

You are given a string s.
Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string s .

Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
'''




s = input()
has_alnum = False
has_alpha = False
has_digit = False
has_lower = False
has_upper = False

for i in s :
    if i.isalnum():
        has_alnum = True
    if i.isalpha():
        has_alpha = True
    if i.isdigit():
        has_digit = True
    if i.islower():
        has_lower = True
    if i.isupper():
        has_upper = True
print(has_alnum)
print(has_alpha)
print(has_digit)
print(has_lower)
print(has_upper)


#OR


'''s = input("enter a number :\n")
for i in s:
    if i.isalnum() or i.isalpha() or i.isdigit() or i.islower()  or i.isupper():
        print("True")'''