def count_inversions(a):
    size = 2
    n = len(a)
    inversions = 0
    while size < n:
        for i in range(0, n/size + 1, size):
            j = i
            k = i+size/2
            curr = i
            temp = []
            while curr < min(i + size, n):
                if temp:
                    if temp < a[k]:
                        new_temp = a[j]
                        a[curr] = temp
                        temp = new_temp
                elif a[k] < a[j]:
                    temp = a[j]
                    a[curr] = a[k]
                    k += 1
                curr += 1
        size += 1
    return inversions

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(count_inversions(arr))
