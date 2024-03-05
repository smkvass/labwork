#Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path.
import os
x = os.getcwd()
path = "../"
dir_list = os.listdir(path)

print("All files and directories in {path} is: ")

if dir_list:
    print(dir_list)
else:
    print("Dont exist such kind of path")