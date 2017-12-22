single_strand = "AGGTGACACCGCAAGCCTTATATTAGC"

res = ""
for i in range(3):
    res += "Frame " + str(i + 1) + ": "
    res += single_strand[0:i]
    if i != 0:
        res += ' '
    triads = [single_strand[x:x + 3] for x in range(i, len(single_strand), 3)]
    res += ' '.join(triads)
    if i != 2:
        res += '\n'

print(res)