class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       num=len(prices)
       if num <=1: return 0
       #顺序遍历
       minv,maxv=float('inf'),0
       profit1,profit2=[0]*num,[0]*num
       #逆序遍历
       nmax,max2v=0,0
       #顺序遍历为当前值减去局部最小值
       #逆序遍历为局部最大值减去当前值
       for i in range(num):
           minv=min(minv,prices[i])
           maxv=max(maxv,prices[i]-minv)
           profit1[i]=maxv

           nmax=max(nmax,prices[num-i-1])
           max2v=max(max2v,nmax-prices[num-i-1])
           profit2[num-i-1]=max2v
       #单笔交易的最大值
       t=maxv
       for j in range(num-1):
           t=max(t,profit1[j]+profit2[j+1])
       return t

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1: return 0
        dp=[[[0,0] for _ in range(3)] for _ in range(len(prices))]
        #j代表交易次数
        #dp[i][j][0]代表第i+1天没有持有股票的利润
        #dp[i][j][1]代表第i+1天持有股票的利润
        for i in range(len(prices)):
            dp[i][0][0]=0
            dp[i][0][1]=-float('inf')
        for j in range(1,3):
            dp[0][j][0]=0
            dp[0][j][1]=-prices[0]

        for i in range(1,len(prices)):
            for j in range(1,3):
              dp[i][j][0]=max(dp[i-1][j][0],dp[i-1][j][1]+prices[i])
              dp[i][j][1]=max(dp[i-1][j][1],dp[i-1][j-1][0]-prices[i])
        return dp[-1][-1][0]
