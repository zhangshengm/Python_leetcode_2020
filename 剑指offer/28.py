# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True

        return self.abc(root.left,root.right)
    def abc(self,a,b)->bool:
        if not a and not b: return True

        if not a or not b or a.val!=b.val: return False
  

        return self.abc(a.left,b.right) and self.abc(a.right,b.left)
        
