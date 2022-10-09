from fractions import Fraction, gcd

def swap_row(m, i, j):
    temp = m[i]
    m[i] = m[j]
    m[j] = temp
    return m

def print_matrix(m):
    for row in m:
        print row

def get_inverse(matrix):
    n = len(matrix)
    aug = [[Fraction(0, 1) for i in range(n)] for j in range(n)]
    for i in range(n):
        aug[i][i] = Fraction(1, 1)
    for i in range(n):
        if matrix[i][i] == 0:
            for j in range(i+1, n):
                if matrix[j][i] != 0:
                    matrix = swap_row(matrix, i, j)
                    aug = swap_row(aug, i, j)
                    break
            assert matrix[i][i] != 0
        prev = matrix[i][i]
        for j in range(n):
            matrix[i][j] /= prev
            aug[i][j] /= prev
        for j in range(i+1, n):
            prev = matrix[j][i]
            for k in range(0, n):
                matrix[j][k] -= matrix[i][k]*prev
                aug[j][k] -= aug[i][k] * prev
    for i in range(n-1, 0, -1):
         for j in range(i-1, -1, -1):
             prev = matrix[j][i]
             for k in range(0, n):
                matrix[j][k] -= matrix[i][k]*prev
                aug[j][k] -= aug[i][k]*prev
    return aug

def answer(m):
    # create Q = recurring to recurring
    # create R = recurring to terminal
    # create N = (I - Q)^-1
    # return top row of NR

    recurring = []
    terminals = []

    for i in range(len(m)):
        reoccurs = False
        for j in range(len(m[i])):
            if i != j and m[i][j] != 0:
                recurring.append(i)
                reoccurs = True
                break
        if not reoccurs:
            terminals.append(i)

    num_rec = len(recurring)
    num_term = len(terminals)

    if num_rec == 0:
        return [1,1]

    Q = [[0 for i in range(num_rec)] for j in range(num_rec)]
    R = [[0 for i in range(num_term)] for j in range(num_rec)]

    #print(recurring)
    #print(terminals)
    for i in range(num_rec):
        total = 0
        for j in range(len(m)):
            total += m[recurring[i]][j]
        for j in range(num_rec):
            Q[i][j] = Fraction(m[recurring[i]][recurring[j]], total)
        for j in range(num_term):
            R[i][j] = Fraction(m[recurring[i]][terminals[j]], total)

    for i in range(num_rec):
        for j in range(num_rec):
            if i == j:
                Q[i][j] = 1 - Q[i][j]
            else:
                Q[i][j] *= -1
    #print Q
    N = get_inverse(Q)
    #print N
    results = []
    denoms = []
    for i in range(num_term):
        result = N[0][0] * R[0][i]
        for j in range(1, num_rec):
            result += N[0][j]*R[j][i]
        results.append(result)
        denoms.append(result.denominator)
    lcm = reduce(lambda x, y: x*y/gcd(x, y), denoms)
    final = []
    for result in results:
        final.append(result.numerator * (lcm/result.denominator))
    final.append(lcm)
    return final

#print answer([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
#print answer([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
print answer([[1, 0, 0], [3, 4, 5], [3, 1, 2]])

# get_inverse([[Fraction(0, 1), Fraction(1, 1), Fraction(2, 1), Fraction(3, 1)],
#              [Fraction(1, 1), Fraction(0, 1), Fraction(2, 1), Fraction(3, 1)],
#              [Fraction(3, 1), Fraction(2, 1), Fraction(0, 1), Fraction(1, 1)],
#              [Fraction(2, 1), Fraction(1, 1), Fraction(3, 1), Fraction(0, 1)]])

