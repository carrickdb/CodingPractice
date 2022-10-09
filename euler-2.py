total = 0
curr = 2
prev = 1
prevprev = 1
while curr < 4000000:
    if curr % 2 == 0:
        total += curr
    prevprev = prev
    prev = curr
    curr = prev + prevprev

print(total)
