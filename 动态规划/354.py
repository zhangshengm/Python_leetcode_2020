class Solution:
    #超出时间限制
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:return 0
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        #dp[k]代表以k个元素结尾的最长递增子序列长度
        dp=[1]*len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1]<envelopes[i][1]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:return 0
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        d=[]
        for num in envelopes:
            if not d or d[-1]<num[1]:
               d.append(num[1])
            else:
                i,j=0,len(d)-1
                f=j
                while i <=j:
                    m=(i+j)//2
                    #尾坐标朝左移动
                    if num[1]<=d[m]: 
                        f=m
                        j=m-1
                    #首坐标向右移动
                    else:
                        i=m+1
                #f为元素num[1]在d中的位置,并替换掉d中对应的元素
                d[f]=num[1]

        return len(d)
