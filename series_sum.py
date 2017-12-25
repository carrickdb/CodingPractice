def series_sum(n):
    if not n:
        return 0.00
    denominator = 1.0
    sum = 0.0
    for i in range(n):
        sum += 1/denominator
        denominator += 3
    return '{:.2f}'.format(sum)


print(series_sum(5))