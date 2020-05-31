class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        True_set = {0}  # 保存已经能正确到达0的城市
        for (i,j) in connections:
            if j in True_set: #如果是(其他节点，已到节点)，直接加入其他节点到已到节点中
                True_set.add(i)
            elif i in True_set:#如果是(已到节点，其他节点)，操作次数加1,加入其他节点到已到节点中
                 res+=1
                 True_set.add(j)
        return res
