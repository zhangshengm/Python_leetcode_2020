class Solution:
    #考虑两种情况:数组全为负数；数组有正数和负数
    def maxSubArray(self, nums: List[int]) -> int:
        i,j,s,s1=0,0,0,[]
        if not nums: return 
        while i <=len(nums)-1 and j<=len(nums)-1:
            s+=nums[j]
            #前面数组之和为正数，则继续寻找最大值
            if s>=0:
               j+=1
               if not s1 or s>s1[-1]:
                 s1.append(s) 
            #前面数组之和为负数，则重新选取第一个数的下标
            else:
               s=0
               i+=1
               j=i
        #如果为空，说明全为负数，取出最大值即可
        if not s1:
            return max(nums)
        return s1[-1]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #f(i)=nums[i], if i=0 or f(i-1)<=0
        #f(i)=f(i-1)+nums[i], if f(i-1)>0
        maxv,sumv=float('-inf'),0
        for i in range(len(nums)):
            if sumv<=0:
                sumv=nums[i]
            else:
                sumv+=nums[i]
            if sumv>maxv:
                maxv=sumv
        return maxv
