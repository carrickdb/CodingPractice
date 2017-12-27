import sys

def make_change(coins, n):
    c = len(coins)
    C = [[0 for i in range(n+1)] for j in range(c+1)]
    for i  in range(c+1):
        C[i][0] = 1
    for i in range(1, c+1):
        for j in range(1, n+1):
            prevSum = j - coins[i-1]
            combo1 = 0
            if prevSum >= 0:
                combo1 = C[i][prevSum]
            C[i][j] = combo1 + C[i-1][j]
    return C[c][n]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))