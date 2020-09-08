class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        flag=[0]*len(primes)
        dp=[0]*n
        dp[0]=1
        for i in range(1,n):
            tmp=float('inf')
            for j in range(len(primes)):
                tmp=min(tmp,dp[flag[j]]*primes[j])
            for j in range(len(primes)):
                if tmp==dp[flag[j]]*primes[j]:
                    flag[j]+=1
            dp[i]=tmp
        # print(dp)
        return dp[-1]
