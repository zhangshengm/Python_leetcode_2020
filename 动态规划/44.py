class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        a,b='#'+s,'#'+p
        la=len(a)
        lb=len(b)
        dp=[[False]*(lb) for _ in range (la)]
        #代表两个空字符匹配成功
        dp[0][0]=True
        for i in range(la):
            for j in range(1,lb):
                if i==0:
                    #第一行元素
                    if j>=1:
                       dp[i][j]=dp[i][j-1] and b[j]=='*'
                #从第二行元素开始
                elif a[i]==b[j] or b[j]=="?":
                    dp[i][j]=dp[i-1][j-1] 

                elif b[j]=='*':
                     dp[i][j]=dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]= False
        return dp[-1][-1]
                    
