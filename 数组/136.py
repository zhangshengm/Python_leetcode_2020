class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashm={}
        for i in range(len(nums)):
            if nums[i] not in hashm:
               hashm[nums[i]]=1
            else:
                hashm[nums[i]]+=1
        return list((hashm.keys()))[list(hashm.values()).index(1)]
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #任何数和0异或是数字本身
        #任何数与自身异或为0
        #异或满足交换律和结合律
        t=0
        for i in range(len(nums)):
            t^=nums[i]
        return t
