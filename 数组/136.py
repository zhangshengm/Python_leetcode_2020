class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashm={}
        for i in range(len(nums)):
            if nums[i] not in hashm:
               hashm[nums[i]]=1
            else:
                hashm[nums[i]]+=1
        return list((hashm.keys()))[list(hashm.values()).index(1)]
