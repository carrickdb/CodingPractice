curr = 600851475143
# curr = 30

n = curr
d = 2
maxFactor = float("-inf")
while d*d <= curr:
    while n % d == 0:
        n /= d
        maxFactor = max(maxFactor, d)
    d += 1

print(maxFactor)
