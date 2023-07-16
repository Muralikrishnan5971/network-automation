
mac_add = list()
with open('macs.txt', 'r') as f:
    content = f.read().splitlines()
    print(content)
    print(len(content))
    content = list(set(content))  # passing the list to a set function removes all duplicates
    # [mac_add.append(x) for x in content if x not in mac_add]

print(content)
print(len(content))

with open('newmacs.txt', 'w') as f:
    f.write("\n".join(content))

"""
or you can iterate over the list content to write into the new file
for mac in content:
    f.write(f"{mac}\n")

    demo

"""

