class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:return 0
        res=0
        #卖出价格
        for i in range(1,len(prices)):
            #卖出价格-最小买入价格
            res=max(res,prices[i]-min(prices[0:i]))
        return res
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       minv=float('inf')
       maxv=0
       #当前值减去局部最小值
       for i in prices:
           minv=min(minv,i)
           maxv=max(maxv,i-minv)
       return maxv

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       if not prices: return 0
       minv=prices[0]
       #dp[i]代表第i天的最大利润
       dp=[0]*(len(prices)+1)
       dp[1]=0
       for i in range(1,len(prices)):
           minv=min(minv,prices[i])
           dp[i+1]=max(dp[i],prices[i]-minv)
       return dp[-1]
