#Write a Python program to list only directories, files and all
#directories, files in a specified path
import os
x = os.getcwd()
path = "../"
dir_list = os.listdir(path)

print("All files and directories in {path} is: ")
dir_list.sort()
print(dir_list)

#print(x)