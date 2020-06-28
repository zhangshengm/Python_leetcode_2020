class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num=0
        for i in range(1,len(prices)):
            tem=prices[i]-prices[i-1]
            if tem>0: num+=tem
        return num
            
