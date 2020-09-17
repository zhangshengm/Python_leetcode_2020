class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(set(nums))*3-sum(nums))//2
        

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=[0]*32
        div=1
        for i in range(31,-1,-1):
          for num in nums:
            if num&div:
               d[i]+=1
          div<<=1
        tmp=1
        res=0
        for j in range(31,-1,-1):
            res+=d[j]%3*tmp
            tmp*=2
        return res




