# Description: This program will read and write to a file
# file = open('spider.txt');
# print(file.readlines())
# file.close();

# Read the file
'''
with open('spider.txt') as file:
    print(file.readlines())
    #not need to close the file
'''
 
'''
with open('spider.txt') as file:
    for line in file:
        print(line.upper()) 
        print(line.strip().upper()) #remove the white space
    #is automatically closed and \n
'''    

'''
file = open('spider.txt');
lines = file.readlines();
file.close();
lines.sort()
print(lines)
'''

# Write to a file

with open('text-write.txt', 'w') as file:
    file.write('I am a spider')
    
''' cheat sheet ref: https://docs.python.org/3/library/functions.html#open'''

# remove the file and rename the file

import os
# os.remove('text-write.txt')
os.path.exists('text-write.txt') # check if the file exists
# os.rename('text-write.txt', 'file-writing.txt')
path = os.path.abspath('file-writing.txt') # get the absolute path of the file
print(path)
print(os.getcwd()) # get the current working directory // PWD command in linux
# print(os.mkdir('new_dir')) # create a new directory or os.chdir('new_dir') # change the directory
print(os.listdir("PyOOP")) # list all the files in the PyOOP directory
print(os.listdir()) # list all the files in the current directory
#os.rmdir('new_dir') # remove the directory

