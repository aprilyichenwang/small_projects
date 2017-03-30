def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    l, w=len(grid), len(grid[0])

    def sum_adjacent(i, j, grid):
        res = 0
        adjacent = (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
        for x, y in adjacent:
            if x < 0 or y < 0 or x == l or y == w or grid[x][ y] == 0:
                res += 1
        return res



    parimeter = 0
    for i in range(0, l):
        for j in range(0, w):
            if grid[i][ j]==1:
                parimeter+=sum_adjacent(i, j, grid)
    return parimeter






print islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
)