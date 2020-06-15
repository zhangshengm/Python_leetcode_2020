class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1:
                    dp[i][j]=dp[i][j-1]+grid[i-1][j-1]
                elif j==1:
                    dp[i][j]=dp[i-1][j]+grid[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
        return dp[-1][-1]
    
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if i==0:
                    if j>=1:
                        grid[i][j]+=grid[i][j-1]
                elif j==0:
                    if i>=1:
                        grid[i][j]+=grid[i-1][j]
                else:
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
