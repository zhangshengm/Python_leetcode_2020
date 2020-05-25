# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.Hash, self.pr = {}, preorder
        for i in range(len(inorder)):
            self.Hash[inorder[i]] = i
        #前序，中序，中序
        return self.recur(0, 0, len(inorder) - 1)

    def recur(self, pre_root, in_left, in_right):
        #规定界限左子树[根节点索引+1,0,根节点-1]，界限右子树[左子树长度+根节点索引+1,根节点+1,len-1]
        if in_left > in_right: return 
        root = TreeNode(self.pr[pre_root]) 
        i = self.Hash[self.pr[pre_root]]   
        root.left = self.recur(pre_root + 1, in_left, i - 1) 
        root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right) 
        return root
