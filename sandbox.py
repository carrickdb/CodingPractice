arr = [0, 1, 2, 2]

n = 2
xor_total = n
for i in range(n-1, -1, -1):
    print(xor_total)
    xor_total ^= i

print(xor_total)

for num in arr:
    xor_total ^= num

print(xor_total)