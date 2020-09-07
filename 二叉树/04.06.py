# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        res=None
        node=root
        #二叉搜索树中某个节点的后继节点一定比某个节点的值要大
        while node:
              if node.val<=p.val:
                  node=node.right
              else:
                  res=node
                  node=node.left
        return res
