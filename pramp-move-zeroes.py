"""
1 0 0 2 3
  i   n

1 0 0 2 0


states:
haven't seen any zeroes yet (currZero == -1, nonZero == -1)
found a zero, need to find later nonzeroes<-|
found later nonzeroes, need to swap --------|

"""

def moveZeroes(arr):
    currZero = -1
    nonZero = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            if nonZero >= 0:
                arr[i] = arr[nonZero]
                arr[nonZero] = 0
                nonZero += 1
            else:
                currZero = i
        elif currZero >= 0:
            for j in range(i+1, len(arr)):
                if arr[j] != 0:
                    nonZero = j
                    break
    return arr


print(moveZeroes([0]))
