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

class Solution:
    #中序遍历，返回K大的节点值
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res=[]
        def recur(root):
            if not root: return
            recur(root.left)
            res.append(root.val)
            recur(root.right)
        
        recur(root)
        return res[len(res)-k]
