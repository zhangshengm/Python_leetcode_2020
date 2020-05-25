# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        t=root.left
        root.left=self.mirrorTree(root.right)
        root.right=self.mirrorTree(t)
        return root
        
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        #根节点放入列表中，它的联系仍然存在
        stack=[root]
        while stack:
            #首次弹出根节点，然后左、右子节点入栈，当前的左右节点在树内交换位置，第二次首先弹出右节点
            node=stack.pop()
            if node.left: stack.append(node.left)
            if node.right:stack.append(node.right)
            node.left,node.right=node.right,node.left
        return root
