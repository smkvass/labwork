#Write a function that computes the volume of a sphere given its radius.
def find_volume():
    pi = 3.14
    R = int(input("Enter a radius: "))
    V = 3/4 * pi * pow(R,3)
    return V
res = find_volume()
print(f"{res}")