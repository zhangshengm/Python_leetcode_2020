class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        #L为最大长度,res为临时长度值
        L,res=1,1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                res+=1
            else:
                L=max(L,res)
                res=1
        #注意最后一个res可能为最大值，所以要判读
        return max(L,res)
