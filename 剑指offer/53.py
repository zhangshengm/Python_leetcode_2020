class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        if hashmap.get(target):
            return hashmap[target]
        else:
            return 0

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findtarget(nums,target):
            i,j=0,len(nums)-1
            while i<=j:
              mid=(i+j)//2
              if nums[mid]<=target:
                  i=mid+1
              else: j=mid-1
            return i

        return findtarget(nums,target)-findtarget(nums,target-1)
