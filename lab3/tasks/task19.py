#Write a function that takes in a list of integers and returns True if it contains 007 in order
def do_it(num):
    a = ""
    for i in range(len(num)):
        if num[i] == 0 or num[i] == 7:
            a = a + str(num[i])
        else:
            continue
        if "007" in a:
            return True
        else:
            return False
        
num = list(map(int, input().split()))
print(do_it(num))