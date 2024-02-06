#Define a function of integers and prints a histogram to the screen. 
#For example, histogram([4, 9, 7]) should print the following:
# **** ********* *******
def histogram(num):
    for i in num:
        print('*' * i)
        
histogram([4,9,7])
    