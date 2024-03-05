#Write a Python program to copy the contents of a file to another file
with open("first.txt", "r") as firsttxt, open("second.txt", "w") as secondtxt:
    #read content from first
    for line in firsttxt:
        #append content to second
        secondtxt.write(line)