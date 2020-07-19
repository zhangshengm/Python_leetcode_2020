class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       if len(prices)<=1: return 0
       #i为当前值下标,profit为最大利润
       i,profit=1,0
       #为局部最小值
       tmp=prices[0]
       while i<len(prices):
            if prices[i]<=tmp:
                tmp=prices[i]
            #t为当前值-局部最小值，为当前利润
            t=prices[i]-tmp
            if t>profit:
                profit=t
            i+=1
       return profit
