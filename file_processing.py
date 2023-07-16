"""
unicode Unicode is an international character encoding standard that provides a unique number 
for every character across languages and scripts, making almost all characters accessible across 
platforms, programs, and devices.

Unicode is a superset of ASCII
first 120 characters are smae for both

most of the unicode characters are encoded UTF-8 or UTF-32

a open() function always return a file object

most commonly used are read, write and append

if mode is not specified, it will open in read only mode

there are two type of files, text and binary files

****TEXT FILE:
text files are structured as a sequence of lines, where each line includes a
sequence of chracters encoded by default using UTF-8 encoding scheme.

Each line is terminated with a special character called EOL,
this is coded using \n

****BINARY FILE:
A binary file is any type of file that is not a text file.

Binary file can only be processed by an application that knows and 
understand the structure of the file
ex: pdf, excel, video, audio etc

open('filename', 'rb')  --> will open the file in binary mode and 'rt' in text mode.

by default python open in text mode

the read() can be used to read a certain number of characters from the file,
instead of entire contents of the file

"""

f = open('scrollmessage.txt')
# content = m.read()
# print(content)     # as any file, we need to close, once we opened.

first_seven = f.read(7)
print(first_seven)

next_four = f.read(4)
print(next_four)
"""
this reads the next four chars, from where it left off from the previous
read function call. Some how python remembers where it read in the file last time.

this is where the concept of cursor comes into play.
The cursor is the position at which we are currently located.
Now we can tell where the cursor is present using the tell function.

in the above example,c
7 + 4 = 11, the cursor is at 11

And if we want to move to a specific position side the file,
we use the seek function

** Another important thing is when m.read() is called the cursor moves from 
the beginning till the end.and calling the m.read() method again will not print a
nything and the cursor is already at the end.

"""
print(f.tell())

f.seek(10)
print(f.tell())    # 10
print(f.read())    # 

print('*' * 50)

# print(m.closed)
# m.close()
# print(m.closed)

