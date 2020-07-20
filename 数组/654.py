class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        t,res=[],[]
        s=0
        for i in range(len(nums)):
            if nums[i] not in t:
                t.append(nums[i])
                #去除重复元素的异或值
                s^=nums[i]
            #找到重复元素
            else:
                 res.append(nums[i])
        #找到缺失元素
        for i in range(1,len(nums)+1):
            s^=i
        res.append(s)
        return res



         
        

          
            
