
#假设超过一半的元素总是存在，如果不存在只需判断maxcount_v出现的次数是否大于n/2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m_a=0
        count=0
        for i in nums:
            #如果相等，个数加一
            if m_a==i:
                count+=1
                continue
            #如果个数为0，初始化，个数等于一
            if count==0:
                m_a=i
                count=1
                continue
            #如果不相等，个数减一
            count-=1
        return m_a
