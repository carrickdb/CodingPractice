filename = "test.txt"

with open(filename, 'w') as f:
    f.write("hello world\nlsdhflsdhf")

with open(filename, 'r') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()
