# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res,path=[],[]
        def recur(root,tar):
            #如果该节点为空，返回
            if not root: return
            path.append(root.val)
            tar-=root.val
            #如果找到满足条件的最后一个叶子结点,将路径加入结果列表
            if tar==0 and not root.left and not root.right: 
                res.append(list(path))
            recur(root.left,tar)
            recur(root.right,tar)
            #当前路径已经判断完，删除最近的一个节点;
            path.pop()
        recur(root,sum)
        return res
