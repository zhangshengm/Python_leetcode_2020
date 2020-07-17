class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        def binary_search(nums,target):
            i,j=0,len(nums)-1
            while i<=j:
              mid=(i+j)//2
              if nums[mid]>target: j=mid-1
              elif nums[mid]<target:
                  i=mid+1
              else:
                  return True
            return False
        #找到目标值的插入位置t
        for i in nums:
            if binary_search(nums,target-i)==True:
                return [i,target-i]
        return False




