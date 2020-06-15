class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #dp[i][j]为长度为i的字符串word1匹配成长度为j的word2需要的最少操作数
        m=len(word1)
        n=len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                else:
                    #如果两个字符相等，则匹配的最少操作数为长度减一的两个字符串的最小操作数
                    if word1[i-1]==word2[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
        return dp[-1][-1]
