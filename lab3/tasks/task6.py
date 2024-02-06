#Write a program which can filter prime numbers in a list by using filter function. 
# Note: Use lambda to define anonymous functions.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num** 1/2) + 1):
        if num % i == 0:
            return False
    return True

