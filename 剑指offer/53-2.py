class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #存在的值和坐标的关系是: nums[i]=i
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        #如果没找到，则缺失值为最大的值
        return i+1
