class Solution:
    def rob(self, nums: List[int]) -> int:
        

        if not nums:return 0
        if len(nums)==1: return nums[0]

        def findmax(nums):
            #dp[i]代表第i个元素结尾的最大累加值
            if len(nums)==1: return nums[0]
            dp=[0]*(len(nums)+1)
            dp[0]=0
            dp[1]=nums[0]
            dp[2]=max(nums[1],nums[0])
            for i in range(3,len(nums)+1):    
                dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
            return max(dp)
        return max(findmax(nums[1:]),findmax(nums[:-1]))

class Solution:
    def rob(self, nums: List[int]) -> int:
      if not nums: return 0
      if len(nums)==1: return nums[0]

      def rob1(nums):
         #pre代表dp[i-2]
         #左边的cur代表dp[i]，右边的cur代表dp[i-1]
         #状态转移方程 dp[i]=max(dp[i-1],dp[i-2]+num[i-1])
         cur, pre = 0, 0
         for num in nums:
            #先调用，再赋值
            cur,pre=max(cur,pre + num),cur
         return cur

      return max(rob1(nums[1:]),rob1(nums[:-1])) 
