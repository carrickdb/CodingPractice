count = {}

with open('text') as f:
    for line in f:
        for char in line.strip():
            count[char] = count.get(char, 0) + 1

print(count)

# e q u a l i t y