def solution(xs):
    greatest_negative = None
    num_nums = 0
    greatest = xs[0]
    total = xs[0]
    for j in xrange(len(xs)):
        if xs[j] > greatest:
            greatest = xs[j]
        if xs[j] != 0:
            num_nums += 1
            total = xs[j]
            if xs[j] < 0:
                greatest_negative = xs[j]
            break
    for i in xrange(j+1, len(xs)):
        if xs[i] != 0:
            num_nums += 1
            total *= xs[i]
        if xs[i] < 0 and xs[i] > greatest_negative:
            greatest_negative = xs[i]
    if total < 0:
        if num_nums > 1:
            total /= greatest_negative
        else:
            return str(greatest)
    return str(total)


xs = [0, 9]
print solution(xs)




