



def answer(M, F):
    m = int(M)
    f = int(F)
    count = 0
    larger = max(m, f)
    smaller = min(m, f)
    while larger > 1 or smaller > 1:
        if larger % smaller == 0:
            if smaller == 1:
                return str(count + larger - 1)
            else:
                return "impossible"
        diff = larger - smaller
        mult = diff / smaller
        larger -= smaller * (mult + 1)
        temp = larger
        larger = smaller
        smaller = temp
        count += mult + 1
    if larger != 1 and smaller != 1:
        return "impossible"
    else:
        return str(count)

'''
7 20
diff = 13
mult = 1
20 -> 20 - 7*2 = 6
count = 2

6 7
diff = 1
mult = 0
7 - 6*1 = 1
count = 3

1 6
count = 8

'''

print answer("434537657868", "9871843238746328746282384629834692387423234923985724852")