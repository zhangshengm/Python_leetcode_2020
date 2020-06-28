class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num=0
        for i in range(1,len(prices)):
            tem=prices[i]-prices[i-1]
            if tem>0: num+=tem
        return num
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       dp=[[0]*2 for _ in range(len(prices))]
       #dp[i][0]代表第i+1天没有持有股票
       #dp[i][1]代表第i+1天持有股票
       dp[0][0]=0
       dp[0][1]=-prices[0]
       for i in range(1,len(prices)):
           dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
           dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
       return dp[-1][0]
