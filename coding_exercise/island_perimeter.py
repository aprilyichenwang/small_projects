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


def get_adjacent_0(i, j, grid):
    # when i, j not in the edge
    adjacent_ls = []
    adjacent_ls.append((grid[i][j + 1], grid[i][j - 1],
                        grid[i - 1][j], grid[i + 1][j]))
    return adjacent_ls[0].count(0)


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # first row, last row- treated different
        # count adjacent 0s- c=c+count_0*1
        # first element, last element, 0 (cannot be fetched, all counts 0)

        grid_padded = [[0 for x in range(len(grid[0]) + 2)] for j in range(len(grid) + 2)]
        peri = 0
        for i in range(1, len(grid_padded) - 1):
            for j in range(1, len(grid_padded[0]) - 1):
                grid_padded[i][j]=grid[i-1][j-1]
        for i in range(1, len(grid_padded) - 1):
            for j in range(1, len(grid_padded[0]) - 1):
                if grid_padded[i][j]==1:
                    peri += get_adjacent_0(i, j, grid_padded)
        return peri


x=Solution()
print x.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
)