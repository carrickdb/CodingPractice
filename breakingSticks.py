from math import sqrt, ceil

sieve = []
memos = {}
global_factors = {}

def createSieve(num):
    global sieve
    sieve = [i for i in range(2, num + 1)]
    for i in range(len(sieve)):
        if i != -1:
            start = sieve[i]*2 - 2
            for j in range(start, len(sieve), sieve[i]):
                #print(j)
                sieve[j] = -1
    sieve[:] = [x for x in sieve if not x == -1]

def getPrimeFactors(num):
    factors = []
    global sieve
    global global_factors
    curr = num
    while curr > 1:
        #print(curr)
        if curr in global_factors:
            factors.extend(global_factors[curr])
            break
        if curr in sieve:
            factors.append(curr)
            break
        prime = sieve[0]
        i = 0
        while i < len(sieve):
            prime = sieve[i]
            if curr % prime == 0:
                factors.append(prime)
                curr //= prime
                break
            i += 1
    factors.sort(reverse=True)
    if num not in global_factors:
        global_factors[num] = factors
    return factors

def getLongest(a):
    global memos
    global sieve
    if a in sieve:
        return a + 1
    primeFactors = getPrimeFactors(a)
    #print(primeFactors)
    res = 1
    i = 0
    curr = a
    num_sticks = 1
    for i in range(len(primeFactors)):
        if curr in memos:
            res += num_sticks * memos[curr]
            break
        num_sticks *= primeFactors[i]
        res += num_sticks
        curr //= primeFactors[i]
        i += 1
    if a not in memos:
        memos[a] = res
    return res

def longestSequence(a):
    #  Return the length of the longest possible sequence of moves.
    total = 0
    for num in a:
        if num == 1:
            total += 1
        else:
            #print("Getting longest sequence for " + str(num))
            total += getLongest(num)
    return total

if __name__ == "__main__":
    #n = int(input().strip())
    n = "656498 874575 10 7 5 12 2 8 820864 6 835290 559277 608745 983061 766719 9 13 608745 15 11 686788 759627 14 1 3 4 686788"
    a = list(map(int, n.split()))


    if max(a) == 1:
        print(1)
    else:
        createSieve(max(a))
        result = longestSequence(a)
        print(result)
