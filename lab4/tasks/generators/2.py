#Write a program using generator to print the even numbers between 0 and 
#`n` in comma separated form where `n` is input from console.
def even_nums(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
          yield i
        i += 1
    
n = int(input())
values = []
for i in even_nums(n):
    values.append(str(i))
    
print(",".join(values))