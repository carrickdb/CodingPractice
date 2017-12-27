def set_end(c2, j, curr_row, lampposts):
    new_end = c2
    for k in range(j + 1, len(curr_row)):
        other_coords = curr_row[k]
        if other_coords[0] < c2:
            if other_coords[1] > c2:
                new_end = other_coords[1]
                del other_coords
                break
            else:
                del other_coords
        else:
            break
    coords[1] = new_end
    return lampposts

n, m, num_trains = map(int, input().strip().split())  #correct
train_rows = {}
lampposts = n * m
for i in range(num_trains):
    train = map(int, input().strip().split())
    r, c1, c2 = train  #correct
    if r in train_rows:
        curr_row = train_rows[r]
        for j in range(len(curr_row)):
            coords = curr_row[j]
            if c1 < coords[0]:
                if c2 < coords[0]:
                    curr_row.insertAt(j, [c1, c2])
                    break
                else:
                    coords[0] = c1
                    set_end(c2, j, curr_row, lampposts)
                    break
            elif c1 <= coords[1]:
                if c2 > coords[1]:
                    set_end(c2, j, curr_row, lampposts)
                break
            elif c1 > coords[1]:
                curr_row.append([c1, c2])
    else:
        train_rows[r] = [[c1, c2]]
        print(train_rows[r])

for k,v in train_rows.items():
    for coords in v:
        lampposts -= coords[1] - coords[0] + 1

print(lampposts)