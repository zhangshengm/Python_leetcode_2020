class Solution:
    def permutation(self, S: str) -> List[str]:
        res=[]
        path=''
        def DFS(nums,path):
            #如果剩余数组长度等于0，将路径添加到集合中
            if len(nums)==0: res.append(path)
            #遍历每条路径
            for i in range(len(nums)):
                DFS(nums[:i]+nums[i+1:],path+nums[i])
        DFS(S,path)
        return res
