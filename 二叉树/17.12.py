# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #由于是左节点，根节点，右节点的顺序，需要一个头节点的右节点指向链表的第一个节点
    
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        self.head = self.current = TreeNode(None)   #定义头结点，最后返回头结点的右子节点
        self.inorder(root)
        return self.head.right

    def inorder(self,root):
        if not root: return 
        self.inorder(root.left)
        #当前节点左节点指向空
        root.left=None
        #前一个节点的右节点指向当前节点
        self.current.right=root
        #更新前一个节点为当前节点
        self.current=root
        self.inorder(root.right)
