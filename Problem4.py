# 4. Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that. 
# 5. Label the program written in problem 4 with comments. 


import os

# Specify the directory path
# directory_path = '/path/to/directory'
directory_path = '\VS Code'


# Get the list of all files and directories
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
