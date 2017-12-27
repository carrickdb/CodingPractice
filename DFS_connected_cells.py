def explore(grid, cell):
    count = 0
    stack  = [cell]
    grid[i][j] = 2
    n = len(grid)
    m = len(grid[0])
    while stack:
        curr = stack.pop()
        count += 1
        i, j = curr
        if i-1 >= 0:
            if grid[i-1][j] == 1:
                grid[i-1][j] = 2
                stack.append((i-1, j))
        if i-1 >=0 and j-1 >= 0:
            if grid[i-1][j-1] == 1:
                grid[i-1][j-1] = 2
                stack.append((i-1, j-1))
        if i-1 >= 0 and j+1 < m:
            if grid[i-1][j+1] == 1:
                grid[i-1][j+1] = 2
                stack.append((i-1, j+1))
        if j-1 >= 0:
            if grid[i][j-1] == 1:
                grid[i][j-1] = 2
                stack.append((i, j-1))
        if j-1 >=0 and i+1 < n:
            if grid[i+1][j-1] == 1:
                grid[i+1][j-1] = 2
                stack.append((i+1, j-1))
        if i+1 < n:
            if grid[i+1][j] == 1:
                grid[i+1][j] = 2
                stack.append((i+1, j))
        if i+1 < n and j+1 < m:
            if grid[i+1][j+1] == 1:
                grid[i+1][j+1] = 2
                stack.append((i+1, j+1))
        if j+1 < m:
            if grid[i][j+1] == 1:
                grid[i][j+1] = 2
                stack.append((i, j+1))
    return count

def getBiggestRegion(grid):
    maxCount = 0
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j]== 1:
                count = explore(grid, (i, j))
                if count > maxCount:
                    maxCount = count
    return maxCount


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
