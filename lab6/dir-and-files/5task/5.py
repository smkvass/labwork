##Write a Python program to write a list to a file
fruits = ['Apple', 'Cherry', 'Peach']
with open("task.txt", "w") as fp:
    for i in fruits:
        ## write each item on a new line
        fp.write("%s\n" % i)
    print('done')