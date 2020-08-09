import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k==0: return [] 
        if k>=len(nums):
           return [max(nums)]
        else:
           #R存每个窗口最大值
           R=[]
           #tmp存数组
           tmp=collections.deque()
           for i in range(k):
               #删除第一个窗口中最大值之前的元素，因为元素重复，对于重复的最大值保留
               while tmp and tmp[-1]<nums[i]:
                     tmp.pop()       
               tmp.append(nums[i])
           R.append(tmp[0])
           for j in range(k,len(nums)):
                #如果出来的元素是临时最大值
                if nums[j-k]==tmp[0]:
                   tmp.popleft()
                #重新整理数组
                while tmp and tmp[-1]<nums[j]:
                      tmp.pop()
                tmp.append(nums[j])
                R.append(tmp[0])
           return R
