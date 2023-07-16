"""
We open a document, do some changes, save it and then close it.

You dont leave a document open as it consumes resources.

Opening file with 'with' is the more efficient way of opening file in python.
Since using this method closes the opened document automatically.

Meaning, if we opena ny file with out the with function, 
we need explicitly call the file.close() in order to close the open document.

"""

# To read file as a list
with open('scrollmessage.txt') as file:
    # content = file.read().splitlines()      # 1. using splitlines()
    # content = file.readlines()              # 2. using readlines()
    content = file.readline()                 # 3. reads first line
    content = file.readline()                 # 4. reads next line

    # print(content)

print(file.closed)

# with open('settings.txt') as f:
#     print(f.readline(), end=" ")

"""
Any iterable can be passed as an argument to the list function, which inturn returns 
a list object.

And python file object is also an iterable.

"""
print("*" * 50)
with open('scrollmessage.txt') as f:
    line_list = list(f)
    print(line_list)
    print(len(line_list))

print("/*" * 70)

with open('scrollmessage.txt') as f:
    for line in f:
        print(line, end="")    # by default it prints a new line character at the end of the line,
                               # using end="" at the end fixes it.
                               