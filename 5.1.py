
def MintoN(M, N, i, j):
    M = M << i
    mask = (1 << (j - i) + 1)
    print "{0:b}".format(mask)
    mask -= 1
    print "{0:b}".format(mask)
    mask = mask << i
    mask = ~mask
    print "{0:b}".format(mask)
    N = N & mask
    return N | M 


print "{0:b}".format(MintoN(0b10011, 0b00000000000, 3, 7))
