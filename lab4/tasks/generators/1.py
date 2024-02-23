#create a generator that generates the squares of 
# numbers up to some number 'N'
"""
def square_nums(N):
    for i in range(N):
        yield i**2
        
for x in square_nums(8):
    print(x)
    """
def num(n):
    for i in range(0, n, 1):
        yield i
    
    
n = int(input())
for x in num(n): 
    print(x) 