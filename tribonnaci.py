def tribonacci(signature, n):
    if n < 3:
        return signature[0:n]
    memo = [0 for i in range(n)]
    memo[0:3] = signature[0:3]
    for i in range(3, n):
        for j in range(3):
            memo[i] += memo[i-j-1]
    return memo


print(tribonacci([0, 1, 1], 6))