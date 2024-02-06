#Write a program able to play the "Guess the number" - game, 
#where the number to be guessed is randomly chosen between 1 and 20. 
#This is how it should work when run in a terminal:
#Hello! What is your name? KBTU Well, KBTU, I am thinking of a number between 1 and 20. Take a guess. 
# 12 Your guess is too low. Take a guess. 16 Your guess is too low. Take a guess. 19 Good job, KBTU! 
# You guessed my number in 3 guesses!
import random
print("Hello! What's your name?")
a = input()
print("Well, " ,a, ",I am thinking of a number betweem 1 and 20.Take a guess")
numbers = random.randint(1, 20)
attempt = 0
while True:
    #num placed into the loop, if it stays in outside it will work infinitely
    num = int(input())
    if num < numbers:
        print("Your guess is too low.Take a guess.")
        attempt += 1 
    elif num > numbers:
        print("Your guess is too high.Take a guess")
        attempt += 1
    else:
        print("You guessed my number in ", attempt, " guesses!")
        break