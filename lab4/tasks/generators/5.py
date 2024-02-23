#Implement a generator that returns all numbers from (n) down to 0
def rev(n):
    for i in range(n, 0, -1):
        yield i
    
n = int(input())
for x in rev(n):
    print(x) 