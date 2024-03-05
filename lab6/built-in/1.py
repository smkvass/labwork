#write a python program with built-in function to multiply all the
#numbers in a list
def multiply(nums):
    res = 1
    for i in nums:
        res *= int(i)
    return res

numbers = list(map(int, input("Enter nums without spaces: ").split(',')))
result = multiply(numbers)
print("The product of element equals:", result)