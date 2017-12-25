n, m, k = map(int, input().strip().split())
train_rows = {}
lampposts = n * m
for i in range(k):
    train = map(int, input().strip().split())
    if m in train_rows:
        for i in train_rows[m]:
            if c1 < coords[0]:
                if c2 < coords[0]:

                    break
                else:

                    break
                if coords[1] < c2:
                    coords[1] = c2
    else:
        train_rows[m] = [[c1, c2]]
        lampposts -= c2 - c1 + 1

print(lampposts)