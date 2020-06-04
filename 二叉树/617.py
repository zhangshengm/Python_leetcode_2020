# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#深度优先搜索
#时间复杂度:O(N),N为两棵树节点的最小值
#空间复杂度:O(N)
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2: 
            return None
        elif t1 and t2:
           temp=t1.val
           t1.val=temp+t2.val
        else:
            if not t1:
               return t2
            if not t2:
                return t1

        t1.left=self.mergeTrees(t1.left,t2.left)
        t1.right=self.mergeTrees(t1.right,t2.right)
        return t1
