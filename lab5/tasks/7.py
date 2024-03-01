#write a python program to convert snake case string to camel case string
def convertion(snake_case):
    str = snake_case.split('_')
    camel_case = str[0] + ''.join(word.capitalize() for word in str[1:])
    return camel_case

string = str(input("Enter a string: "))
res = convertion(string)
print("Snake Case:", string)
print("Camel Case: ", res)