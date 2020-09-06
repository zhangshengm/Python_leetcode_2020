# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_height(root):
            if not root:return 0
            return max(check_height(root.left),check_height(root.right))+1
        
        if not root: return True
         #判断根节点左右子树的高度相差如果大于1，则是不平衡树
        if abs(check_height(root.left)-check_height(root.right))>1:
           return False
        #一次判断左子树是不是平衡子树，右子树是不是平衡子树，当左右子树都是平衡树，则是平衡子树
        return self.isBalanced(root.left) and self.isBalanced(root.right)
