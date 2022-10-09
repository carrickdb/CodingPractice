"""
naive solution:
for each i:
    for each j starting at i + 2:


n choose 2?
n^2 * n (for converting number into binary)
  i
0 1 2 3 4
"""
def threeEqualParts(arr):
    #        0 1 2 3 4
    # arr = [0,1,0,1,1]
    for i in range(len(arr) - 2):
        first_num_str = list(map(str, arr[:i+1]))
        first_num = ''.join(first_num_str)
        first_num = int(first_num, 2)
        for j in range(i+2, len(arr)):
            print("j", j)
            second_num_str = list(map(str, arr[i+1:j]))
            second_num = ''.join(second_num_str)
            second_num = int(second_num, 2)
            if second_num > first_num:
                break
            if second_num < first_num:
                continue
            third_num_str = list(map(str, arr[j:]))
            third_num = ''.join(third_num_str)
            third_num = int(third_num, 2)
            if second_num > third_num:
                break
            if second_num == third_num:
                return [i, j]
    return [-1, -1]

arr = [0,1,0,1,1]
print(threeEqualParts(arr))
