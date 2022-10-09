def grey_code(n):

    def grey_code_pattern(m):
        if m == 1:
            return [0]
        pattern = grey_code_pattern(m-1)
        return pattern + [m-1] + pattern

    full_pattern = grey_code_pattern(n)
    curr = 0
    ret = [0]
    for flip in full_pattern:
        prev = ret[-1]
        mask = 1 << flip
        next_num = prev ^ mask
        ret.append(next_num)
    return ret

grey_code_sequence = grey_code(4)

for num in grey_code_sequence:
    print(format(num, 'b'))

"""
000
001 0
011 1
010 0
110 2
111 0
101 1
100 0

0000
0001 1
0011 2
0010 1
0110 3
0111 1
0101 2
0100 1
1100 4
1101 1
1111 2
1110 1
1010 3
1011 1
1001 2
1000 1


res = [0]
for i in range(n):
    res += [x|(1<<i) for x in res[::-1]]
return res

1 0

10

0
0 1
0 1 11 01
0 1 11 01  



"""
