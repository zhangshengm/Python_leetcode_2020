class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #存在的值和坐标的关系是: nums[i]=i
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        #如果没找到，则缺失值为最大的值
        return i+1
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i,j=0,len(nums)-1
        while i<=j:
            mid=(i+j)//2
            #如果数组某位置的值等于该位置，说明缺失值在位置之后
            if nums[mid]==mid: i=mid+1
            #如果数组某位置的值等于该位置，说明缺失值在位置之前
            else:
                j=mid-1
        return j+1
        
