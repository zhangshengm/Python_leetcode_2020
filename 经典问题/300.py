class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #res代表最长子序列的长度
        tail,res=[0]*len(nums),0

        for num in nums:
            i,j=0,res
            while i<j:
                  m=(i+j)//2
                  if tail[m] < num: i=m+1
                  else:
                      j=m
            #要么把大的元素插入到后面；要么用小的元素替换
            tail[i]=num
            #插入元素的位置到末尾了,该情况下，最长上升子序列长度加1
            if i==res: res+=1
        return res
