#出现次数大于1/3次数，记得先判断是否相等，再判断个数是否为0
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m_a,count_a=0,0
        m_b,count_b=0,0
        for i in nums:
            #如果相等，个数加一
            if m_a==i:
                count_a+=1
                continue
            if m_b==i:
                count_b+=1
                continue
            #如果个数为0，初始化，个数等于一
            if count_a==0:
                m_a=i
                count_a=1
                continue
            if count_b==0:
                m_b=i
                count_b=1
                continue
           
            #如果不相等，个数减一
            count_a-=1
            count_b-=1
        count_a,count_b=0,0
        for i in nums:
            if i==m_a:
              count_a+=1
            elif i==m_b:
              count_b+=1
        res=[]
        if count_a>(len(nums)//3):
            res.append(m_a)
        if count_b>(len(nums)//3):
            res.append(m_b)
        return res
