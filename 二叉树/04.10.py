# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def DFS(t1,t2):
            if t2==None:
                return True
            elif t1==None:
                return False
            elif t2.val!=t1.val:
                return False
            else:
                return DFS(t1.left,t2.left) and DFS(t1.right,t2.right)
        #如果要判断的树为空，则是子树
        if t2==None:
            return True
        #如果树不为空，主树为空则不是子树
        elif t1==None:
            return False
        #t2要么是t1的子树，要么是t1的左子树的子树，要么是t1的右子树的子树，要么都不是
        return DFS(t1,t2) or self.checkSubTree(t1.left,t2) or self.checkSubTree(t1.right,t2)
