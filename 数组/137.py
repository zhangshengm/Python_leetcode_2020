class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s,sum_n=set(),0
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            sum_n+=nums[i]
        return (3*sum(s)-sum_n)//2  
        
        
