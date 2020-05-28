# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #后序遍历
    def maxDepth(self, root: TreeNode) -> int:

        if not root: return 0
        return max(1+self.maxDepth(root.left),1+self.maxDepth(root.right))
        
class Solution:
    #层序遍历
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        stack,flag=[root],0
        while stack:
            tmp=[]
            for node in stack:
                if node.left:  tmp.append(node.left)
                if node.right: tmp.append(node.right)
            stack=tmp
            flag+=1
        return flag
