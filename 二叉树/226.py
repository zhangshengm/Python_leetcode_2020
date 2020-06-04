# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#时间复杂度:O(N)
#空间复杂度:O(N)
#递归
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        temp=root.left
        root.left=self.invertTree(root.right)
        root.right=self.invertTree(temp)
        return root
