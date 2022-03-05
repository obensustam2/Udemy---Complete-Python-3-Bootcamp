file_path = 'myfile.txt'

with open(file_path, mode='w') as a:  # create & write to file
    a.write('Merhaba')

with open(file_path, mode='a') as b: # append to file
    b.write('\nAcun Abi')

with open(file_path, mode='r') as c: # read the file
    print(c.read())

print()

with open(file_path, mode='r') as d: # read the file and create a list
    print(d.readlines())



