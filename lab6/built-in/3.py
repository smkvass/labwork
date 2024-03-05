#Write a Python program with builtin function that checks whether 
#a passed string is palindrome or not
def is_palindrome(s):
    return s == s[::-1]

s = str(input())
res = is_palindrome(s)
if res:
    print("Yes")
else:
    print("No")
    
#a = '1234'
# a[::-1]
#'4321'
