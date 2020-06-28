class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       if len(prices)<=1: return 0
       dp=[[0]*2 for _ in range(len(prices))]
       #dp[i][0]代表第i+1天没有持有股票
       #dp[i][1]代表第i+1天持有股票
       dp[0][0]=0
       dp[0][1]=-prices[0]
       #第二天没有股票: 昨天买了股票，今天卖了；昨天没有买，今天也没有买
       dp[1][0]=max(dp[0][1]+prices[1],dp[0][0])
       #第二天持有股票: 昨天买了股票；昨天没有买,今天买了股票
       dp[1][1]=max(dp[0][1],dp[0][0]-prices[1])
       for i in range(2,len(prices)):
           dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
           dp[i][1]=max(dp[i-1][1],dp[i-2][0]-prices[i])
       return dp[-1][0]
