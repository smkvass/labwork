#write a python program to convert a given camel case string to snake
def conversion(camel_case):
    snake_case = ''.join(['_' + char.lower() if char.isupper() else char for char in camel_case])
    return snake_case.lstrip('_')

string = str(input("Enter a string: "))
res = conversion(string)
print("Snake Case: ", res)