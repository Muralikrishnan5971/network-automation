"""
this is an example of relative path

relative means, relative to the current working directory

"""

msg = open('./../settings.txt')   # --> also can be written as ../settings.txt
print(msg.read())