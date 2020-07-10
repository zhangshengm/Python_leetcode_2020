class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t=(len(nums)-1)//2
        nums.sort()
        return nums[t]
        
        
