class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        tb = list()
        lr = list()
        count = 0
        tGrid = zip(*grid)
        for l in grid:
            lr.append(max(l))
            
        for l in tGrid:
            tb.append(max(l))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = count - grid[i][j] + min([tb[i],lr[j]])
        # print(tb)
        # print(lr)
        # print(count)
        return count