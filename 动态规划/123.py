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
    
class Stock:
    def maxProfit(self, prices, n):
        #正序，当前值-最小值,
        #逆序，最大值-当前值
        if n<=1:
           return 0
        res_1,res_2=[0]*(n),[0]*(n)
        tmp1,tmp2=prices[0],prices[-1]
        m1,m2=0,0
        for i in range(1,n):
            if prices[i]<=tmp1:
               tmp1=prices[i]
            else:
               m1=max(m1,prices[i]-tmp1)
               res_1[i]=m1
        for j in range(n-2,-1,-1):
            if prices[j]>=tmp2:
               tmp2=prices[j]
            else:
               m2=max(m2,tmp2-prices[j])
               res_2[j]=m2
        t=max(res_1[-1],res_2[0])
        for k in range(0,n-1):
            t=max(t,res_1[k]+res_2[k+1])
        return t
