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

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        #dp[i]表示以第i+1个数字结尾的连续递增序列的最大长度
        dp=[1]*len(nums)
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
               dp[i+1]=max(dp[i],dp[i]+1)

        return max(dp)
    
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        # pre,res=1,1
        res,af=1,0
        for i in range(len(nums)):
            #保证i到末尾,i定位到第一个不符合的数
            if i>=1 and nums[i-1]>=nums[i]: 
                #af代表首指针
                af=i
            res=max(res,i-af+1)
               
        return res
