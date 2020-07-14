class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        dp=[[0]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==0:
                    if j>0:
                      dp[i][j]=dp[i][j-1]+grid[i][j]
                elif j==0:
                    if i>0:
                       dp[i][j]=dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])+grid[i][j]
        return dp[-1][-1]

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        # dp=[[0]*n for _ in range(m)]
        # dp[0][0]=grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==0:
                    if j>0:
                      grid[i][j]=grid[i][j-1]+grid[i][j]
                elif j==0:
                    if i>0:
                      grid[i][j]=grid[i-1][j]+grid[i][j]
                else:
                    grid[i][j]=max(grid[i][j-1],grid[i-1][j])+grid[i][j]
        return grid[-1][-1]
