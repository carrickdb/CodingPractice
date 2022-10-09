def spiral(width):
    currX, currY = 0, 0
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    currDelta = 0
    while width > 0:
        if width == 1:
            print("(" + str(currX) + "," + str(currY) + ")")
            return
        for j in range(4):
            deltaX, deltaY = deltas[currDelta]
            for i in range(width):
                if j == 3 and i == width-2:
                    print("(" + str(currX) + "," + str(currY) + ")")
                    width -= 2
                    currX += 1
                    currDelta = (currDelta + 1) % 4
                    continue
                else:
                    if i < width - 1:
                        print("(" + str(currX) + "," + str(currY) + ")")
                        currX += deltaX
                        currY += deltaY
                    if i == width - 1:
                        currDelta = (currDelta + 1) % 4


"""
765
8 4
123

currX = 0
currY = 1

j = 3
i = 1

"""


spiral(4)



"""
Start at 0,0
alternate incrementing/decrementing x and y
increment/decrement x or y until width of square or width-1 for last edge
decrement width of square
"""
