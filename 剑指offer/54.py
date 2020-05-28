# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res=[]
        node=[root]
        while node:
            t=[]
            for i in node:
                res.append(i.val)
                if i.left:
                   t.append(i.left)
                if i.right:
                   t.append(i.right)
            node=t
        res.sort()
        return res[len(res)-k]

