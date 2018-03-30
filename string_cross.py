horizontal = "ab"

vertical = "ba"

charcount = {}

for char in horizontal:
    charcount[char] = charcount.get(char, 0) + 1

horiz_line = -1
num_spaces = 0

for i in range(len(vertical)):
    curr = vertical[i]
    if curr in horizontal:
        # print horizontal string on i'th line
        # find index j of curr in horizontal
        # add j spaces to beginning of chars in vertical
        # skip i'th vertical character
        horiz_line = i
        for j in range(len(horizontal)):
            if horizontal[j] == curr:
                num_spaces = j
                break
        break

if horiz_line != -1:
    spaces = ' ' * num_spaces
    for i in range(horiz_line):
        print(spaces + vertical[i])
    print(horizontal)
    for i in range(len(vertical) - horiz_line -1):
        print(spaces + vertical[i + horiz_line + 1])
else:
    print("no horizline")