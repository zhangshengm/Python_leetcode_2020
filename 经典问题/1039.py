class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        L=len(A) 
        #dp[i][j]第i个角到第j个角的最小三角形乘积
        dp=[[float('inf')]*L for _ in range(L)]
        #相邻角
        for i in range(L):
            for j in range(i-1,-1,-1):
                if i-j<2:
                   dp[j][i]=0
                else:
                    #取位于首尾值中间的值，A[j]*A[k]*A[i]为划分的三角形+加上首部三角形最小值和尾部三角形最小值
                    for k in range(j+1,i):

                        dp[j][i]=min(dp[j][i],A[j]*A[k]*A[i]+dp[j][k]+dp[k][i])
        return dp[0][L-1]
