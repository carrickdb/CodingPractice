from fractions import gcd, Fraction

def answer(pegs):
    length = len(pegs)
    augment_side = []
    for i in xrange(length-1):
        augment_side.append(pegs[i+1] - pegs[i])
    total = 0
    for num in augment_side:
        total = num - total
    if length % 2 == 1:
        #print total
        if total >= 0:
            return [-1, -1]
        result = Fraction(total*-2, 1)
    else:
        if total <= 0:
            return [-1, -1]
        two = Fraction(2, 1)
        result = Fraction(total, 3)*two
    gear = result
    for i in xrange(length-1):
        curr = Fraction(pegs[i], 1)
        nxt = Fraction(pegs[i+1], 1)
        if curr + gear >= nxt:
            return [-1, -1]
        gear = nxt - curr - gear
    if result.numerator < result.denominator:
        return [-1, -1]
    return [result.numerator, result.denominator]

print answer([1, 4, 6, 11])

'''
1 0 0 -2 0
1 1 0  0 3
0 1 1  0 2
0 0 1  1 5

    for i in xrange(length-1):
        curr = Fraction(pegs[i], 1)
        nxt = Fraction(pegs[i+1], 1)
        if curr + gear >= nxt:
            return [-1, -1]
        gear = nxt - curr - gear

10 passes, 7 fails:
    length = len(pegs)
    augment_side = []
    for i in xrange(length-1):
        augment_side.append(pegs[i+1] - pegs[i])
    total = 0
    for num in augment_side:
        total = num - total
    if length % 2 == 1:
        #print total
        if total >= 0:
            return [-1, -1]
        result = Fraction(total*-2, 1)
    else:
        if total <= 0:
            return [-1, -1]
        two = Fraction(2, 1)
        result = Fraction(total, 3)*two
    gear = result
    for i in xrange(length-1):
        curr = Fraction(pegs[i], 1)
        nxt = Fraction(pegs[i+1], 1)
        if curr + gear >= nxt:
            return [-1, -1]
        gear = nxt - curr - gear
    if result.numerator < result.denominator:
        return [-1, -1]
    return [result.numerator, result.denominator]



7 passes, 10 fails:
    length = len(pegs)
    augment_side = []
    for i in xrange(length-1):
        augment_side.append(pegs[i+1] - pegs[i])
    total = 0
    for num in augment_side:
        total = num - total
    if length % 2 == 1:
        #print total
        if total >= 0:
            return [-1, -1]
        result = Fraction(total*-2, 1)
    else:
        if total <= 0:
            return [-1, -1]
        two = Fraction(2, 1)
        result = Fraction(total, 3)*two
    gear = result
    for i in xrange(length-1):
        curr = Fraction(pegs[i], 1)
        if curr + gear >= Fraction(pegs[i+1], 1):
            return [-1, -1]
    return [result.numerator, result.denominator]

'''

    # g[0] = 2*g[n]
    # g[i] + g[i+1] = pegs[i+1] - pegs[i]
    # 11 20 --> 3x = 9, x = 3, y = 6
    # 0 3 5 --> a+b = 3, b + c = 2, a - 2c = 0
    # 2c+b = 3, b+c = 2
    # 2c + 2-c = 3
    # c+2 = 3, c = 1, a = 2, b = 1
    # 1 0 -2 0
    # 1 1 0  3
    # 0 1 1  2

    # 1 0 -2 0
    # 0 1  2 3
    # 0 0 -1 -1

    # 4 30 50
    # 1 0 -2 0
    # 1 1 0  26


    # 4 17 50
    # 1 0 0 -2 0
    # 1 1 0  0 13
    # 0 1 1  0 33
    # 0 0 1  1 53

    # 1 0 -2 0
    # 0 1  2 13
    # 0 0  -1 20

    # g = [[0 for i in xrange(len(pegs) + 1)] for j in xrange(len(pegs))]
    # g[0][0] = 1
    # g[0][length-1] = -2
    # for i in xrange(1, length):
    #     g[i][length] = pegs[i] - pegs[i-1]
    #     g[i][i-1] = 1
    #     g[i][i] = 1
    #     print g[i]
    # for i in xrange(length-1):
    #     for j in xrange(length+1):
    #         g[i+1][j] -= g[i][j]
    # if g[length-1][length-1] == 0:
    #     if g[length-1][length] == 0:
    #         return [1, 1]
    #     else:
    #         return [-1, -1]
    # if (g[length-1][length-1] < 0 and g[length-1][length] > 0) or \
    #     (g[length - 1][length - 1] > 0 and g[length - 1][length] < 0):
    #     return [-1, -1]
    # x = Fraction(g[length-1][length], g[length-1][length-1])
    # print "x", x
    # two = Fraction(2, 1)
    # result = two * x



