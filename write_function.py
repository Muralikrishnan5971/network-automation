"""
writing to text files

The write function does not add a new line character
Also if the mentioned file does not exist, it creates one,
otherwise it overwrites the file.

open with 'a' will append content at the end of the line.

'w' will overwrite

"""

with open('dummy.txt', 'w') as f:
    f.write("This is a dummy file \n")
    f.write("Overwrting line")

with open('dummy.txt', '') as f:
    f.write("Adding the first line using r+")