#Write a Python program that invoke square root function after 
#specific milliseconds
import time
import math

def sqrt():
    num = float(input("Enter the number: "))
    res = math.sqrt(num)
    print("Square root equals: ", res)
    
sec = 5000
time.sleep(sec/ 1000.0)

sqrt()