class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m=len(triangle)

        #     # if i==0:
            #        dp[i]=triangle[i][0]
        for i in range(m-2,-1,-1):
            #倒着累加和，原三角形第i层的值改为：第i层到第i+1层的最小值
            for j in range(len(triangle[i])):
                  triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])

        return triangle[0][0]
         
