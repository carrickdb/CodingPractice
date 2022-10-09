def checkMove(board, rMove, cMove, color):
    """
    for each direction:
        if adjacent cell is the same color:
            continue
        while next cell is the same color:
            advance to next cell in same direction
        if the next cell is the same color as `color`:
            return true
    return false
    """
    changes = [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    def nextCell(direction, currRow, currCol):
        rowChange, colChange = changes[direction]
        return currRow + rowChange, currCol + colChange

    def otherColor(color):
        return "W" if color == "B" else "B"

    def outOfBounds(board, r, c):
        return r < 0 or r >= len(board) or \
               c < 0 or c >= len(board[0])

    for direction in range(len(changes)):
        nextRow, nextCol = nextCell(direction, rMove, cMove)
        if outOfBounds(board, nextRow, nextCol) or \
           board[nextRow][nextCol] != otherColor(color):
            continue
        next = False
        while board[nextRow][nextCol] == otherColor(color):
            nextRow, nextCol = nextCell(direction, nextRow, nextCol)
            if outOfBounds(board, nextRow, nextCol):
                next = True
                break
        if not next and board[nextRow][nextCol] == color:
            return True
    return False

# board = [[".","W","B",".",".",".",".","."],
#          [".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".","."],
#          [".",".",".",".",".",".",".","."]]
# rMove = 0
# cMove = 0
# color = "B" # true

board = [[".",".",".","B",".",".",".","."],
         [".",".",".","W",".",".",".","."],
         [".",".",".","W",".",".",".","."],
         [".",".",".","W",".",".",".","."],
         ["W","B","B",".","W","W","W","B"],
         [".",".",".","B",".",".",".","."],
         [".",".",".","B",".",".",".","."],
         [".",".",".","W",".",".",".","."]]
rMove = 4
cMove = 3
color = "B"

board = [[".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."]]
rMove = 0
cMove = 0
color = "B" # false

board = [[".","W",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."]]
rMove = 0
cMove = 0
color = "W" # false

board = [[".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".","."],
      [".","B",".",".",".",".",".","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".","."]]
rMove = 2
cMove = 1
color = "B" # false

board = [[".",".",".",".",".",".",".","."],
    [".","B",".",".","W",".",".","."],
    [".",".","W",".",".",".",".","."],
    [".",".",".","W","B",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".","B","W",".","."],
    [".",".",".",".",".",".","W","."],
    [".",".",".",".",".",".",".","B"]]
rMove = 4
cMove = 4
color = "W"

board = [["W","B","W",".",".","W","W","."],["W","B",".","W","W","W","B","W"],[".","B","B",".","B","W","B","W"],[".",".","B","B","B","W","W","."],["B","B",".","B",".",".",".","B"],[".","W","B",".",".","B",".","B"],[".","W",".","W",".","W","B","W"],["W",".","B",".","W","W","B","."]]
rMove = 4
cMove = 6
color = "W"

print(checkMove(board, rMove, cMove, color))
