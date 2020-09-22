class Solution:
    #在数组中出现超过一半的数字，始终存在
    def majorityElement(self, nums: List[int]) -> int:
        index=nums[0]
        count=1
        for num in nums:
            if num==index:
                count+=1
            else:
                count-=1
            if count<=0:
                index=num
                count=1           
        return index
