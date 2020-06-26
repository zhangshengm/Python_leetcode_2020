class Solution:
    #超出时间限制
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:return 0
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        #dp[k]代表以k个元素结尾的最长递增子序列长度
        dp=[1]*len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1]<envelopes[i][1]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
