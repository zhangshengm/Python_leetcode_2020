# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
             #两个节点在右子树
              if root.val<p.val and root.val <q.val:
                 root=root.right
              #两个节点在左子树
              elif root.val >p.val and root.val >q.val:
                 root=root.left
              else: break
        return root
   
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val<q.val: p,q=q,p
        while root:
             #两个节点在右子树
              if root.val <q.val:
                 root=root.right
              #两个节点在左子树
              elif root.val >p.val:
                 root=root.left
              else: break
        return root
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

             #两个节点在右子树
        if root.val<p.val and root.val <q.val:
               return  self.lowestCommonAncestor( root.right,p,q)   
              #两个节点在左子树
        if root.val >p.val and root.val >q.val:
               return  self.lowestCommonAncestor( root.left,p,q)   
        return root

