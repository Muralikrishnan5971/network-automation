with open('configuration.txt') as f:
    file_list = f.read().splitlines()
    # print(file_list)
    devices = []
    for file in file_list[1:3]:
        devices.append(file.split(':'))
    print(devices[1][4])

    # we can do list slicing as done above 

    for device in devices:
        print(f"pinging {device[1]}")