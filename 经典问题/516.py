class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        #dp[j][i]从第j+1个字符到第i+1个字符的最大回文子序列长度
        #注意dp[i][j]=dp[j][i]，对称矩阵求一半
        dp=[[0]*n for _ in range(n)]
          
        for i in range(n):
            #只有一个字符时，长度都为1
            dp[i][i]=1
            for j in range(i-1,-1,-1):
                if s[i]==s[j]:
                   #等于第j个字符到第i个字符中间的字符串的最大回文长度+2
                   dp[j][i]=2+dp[j+1][i-1]
                else:
                    #如果不相等
                   dp[j][i]=max(dp[j+1][i],dp[j][i-1])
                   
        return dp[0][n-1]
