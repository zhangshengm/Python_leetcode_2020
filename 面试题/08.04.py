class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #如果nums中有重复元素，先去重复，set()再转list
        if not nums: return []
        len_nums=len(nums)
        res=[]
        def DFS(tmp,new_nums):
            if len(tmp)>=0 and len(tmp)<len_nums:
               res.append(tmp)
            for j in range(len(new_nums)):
                DFS(tmp+[new_nums[j]],new_nums[j+1:])
        DFS([],nums)        
        res.append(nums)
        return res
