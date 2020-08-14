class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
         dp={}
         #dp[目标下标，目标值-当前值]=dp.get((当前下标，目标值-当前值),1)+1
         for i in range(len(A)-1):
             for j in range(i+1,len(A)):
                 dp[j,A[j]-A[i]]=dp.get((i,A[j]-A[i]),1)+1
         return max(dp.values())
                 
