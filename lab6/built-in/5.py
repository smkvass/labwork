#Write a Python program with builtin function that returns True 
#if all elements of the tuple are true.
def check_tuple(a):
    return all(x == True for x in a) #generator

tuple_input = tuple(input("Enter elements of tuple without spaces: ").split(','))

check = check_tuple(tuple_input)
print(check)