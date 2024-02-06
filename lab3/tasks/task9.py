#Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm.
#How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
         rabbits = numheads - chickens
         if 2 * chickens + 4 * rabbits == numlegs:
           return chickens, rabbits
    return None
numheads = 35
numlegs = 94
res = solve(numheads, numlegs)

if res:
    num_chickens, num_rabbits = res
    print(f"Chickens: {num_chickens}, Rabbits: {num_rabbits}")
else:
    print("No solution found.")
    