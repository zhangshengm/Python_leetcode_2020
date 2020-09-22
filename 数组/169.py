class Solution:
    #假设超过一半的元素总是存在，如果不存在只需判断maxcount_v出现的次数是否大于n/2
    def majorityElement(self, nums: List[int]) -> int:
        maxcount_v=0
        count=0
        for i in nums:
            if count==0:
                maxcount_v=i
            if maxcount_v==i:
                count+=1
            else:
                count-=1
        return maxcount_v
