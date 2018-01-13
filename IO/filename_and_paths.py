import os
cwd = os.getcwd()
print(cwd) # return current working directory


# relative path and obsolute path
print(os.path.abspath('test_for_io.txt'))

# to check if a file or directory exists
print(os.path.exists('test_for_io.txt')) # True

# if exist, os.path.isdir to check if it is a directory
print(os.path.isdir('test_for_io.txt')) # False

# Similarly, os.path.isfile checks whether it’s a file.
print(os.path.isfile('test_for_io.txt')) # True

# os.listdir returns a list of 
# the files (and other directories) in the given directory
print(os.listdir('./'))
