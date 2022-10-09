def answer(x, y):
    longer = x
    shorter = y
    if len(y) > len(x):
        longer = y
        shorter = x
    arr = [0 for i in xrange(2001)]
    for num in shorter:
        arr[num + 1000] = 1
    for num in longer:
        if arr[num+1000] == 0:
            return num


x = [1000]
y = [-1000, 1000]

print answer(x, y)
