# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root: return [[]]
        res=[]
        #当前路径下的最后一个节点，供选择的下一个节点集合，已保存的路径
        def DFS(root,select,path):
            if root.left:
                select.append(root.left)
            if root.right:
                select.append(root.right)
            if not select:
               res.append(path)
               return
            #从select中选择一个节点，其他节点作为tmp来更新select
            for i,node in enumerate(select):
                tmp=select[:i]+select[i+1:]
                DFS(node,tmp,path+[node.val])
        DFS(root,[],[root.val])
        return res
