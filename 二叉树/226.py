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
    
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        head=[root]
        while head:
              s1=[]
              for node in head:
                  t=node.left
                  node.left=node.right
                  node.right=t
                  if node.left:
                      s1.append(node.left)
                  if node.right:
                      s1.append(node.right)
              head=s1
        return root
    
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
       
        head=[root]
        while head:
              node=head.pop()
            #   t=node.left
              node.left,node.right=node.right,node.left
            #   node.right=t
              if node.left:
                      head.append(node.left)
              if node.right:
                      head.append(node.right)

        return root
