#Implement a generator called `squares` to yield the square 
# of all numbers from (a) to (b). Test it with a "for" loop and 
# print each of the yielded values
def square_numbers(a, b):
    while a <= b:
        yield a ** 2
        a += 1
        
        
a = int(input("Enter a: "))
b = int(input("Enter b: "))
for x in square_numbers(a, b):
    print(x)