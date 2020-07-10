class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t=(len(nums)-1)//2
        nums.sort()
        return nums[t]
        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        t={}
        for i in nums:
            if i not in t:
                t[i]=1
            else:
                t[i]+=1
                if t[i]>(len(nums)//2): return i
                
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #给众数设置为1票,其他数为-1票
        vote=0
        for i in nums:
            #当投票数归零时，x设置为众数
            if vote==0:  x=i
            #如果遇到其他数，投票数减一
            if i!=x:
                vote-=1
            #如果遇到其他数，投票数加一
            else:
                vote+=1
        return x 
