def answer(start, length):
    curr = start
    curr_len = length
    xor = 0
    for i in xrange(length):
        if curr_len == 1:
            xor ^= curr
        elif curr % 2 == 1:
            if curr_len % 2 == 1:
                # start odd, length odd
                # if (length-1)/2 even -> first
                # else first ^ 1
                if ((curr_len-1)/2) % 2 == 0:
                    xor ^= curr
                else:
                    xor ^= curr ^ 1
            else:
                # start odd, length even
                # if (length-2)/2 even -> first ^ last
                # else first ^ last ^ 1
                if (curr_len-2)/2 % 2 == 0:
                    xor ^= curr ^ (curr + curr_len - 1)
                else:
                    xor ^= curr ^ (curr + curr_len - 1) ^ 1
        else:
            if curr_len % 2 == 1:
                # start even, length odd
                    # if (length-1)/2 even -> last one
                    # else 1 ^ last one
                if ((curr_len-1)/2) % 2 == 0:
                    xor ^= curr + curr_len - 1
                else:
                    xor ^= 1 ^ (curr + curr_len - 1)
            else:
                # start even, length even
                    # length/2 even -> 0 (do nothing)
                    # else 1
                if (curr_len/2) % 2 == 1:
                    xor ^= 1
        print xor
        curr += length
        curr_len -= 1
    return xor
'''
curr = 0
curr_len = 3
i = 0
xor = 0 ^ 2 = 2

curr = 3
curr_len = 2
i = 1
xor = 2 ^ 3 ^ 1 ^ 4 = 5

curr

'''

print answer(17, 4)