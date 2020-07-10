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
                
