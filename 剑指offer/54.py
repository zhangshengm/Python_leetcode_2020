# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res=[]
        node=[root]
        while node:
            t=[]
            for i in node:
                res.append(i.val)
                if i.left:
                   t.append(i.left)
                if i.right:
                   t.append(i.right)
            node=t
        res.sort()
        return res[len(res)-k]

class Solution:
    #中序遍历，返回K大的节点值
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res=[]
        def recur(root):
            if not root: return
            recur(root.left)
            res.append(root.val)
            recur(root.right)
        
        recur(root)
        return res[len(res)-k]

class Solution:
    #中序遍历的倒序（第几大），返回第K-1个值,只存到第k-1个值
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k=k
        res=[]
        def recur(root):
            if not root: return
            if len(res)==self.k:
               return
            recur(root.right)
            res.append(root.val)
            recur(root.left)
        
        recur(root)
        return res[k-1]
    
 class Solution:
    #中序遍历的倒序，只存满足要求的一个值
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k=k
        self.res=0
        def recur(root):
            if not root: return
            #如果找到了第K大的值，则返回
            if self.k==0: return
            recur(root.right)
            self.k-=1
            #如果找到了第K大的值，赋值给当前值
            if self.k==0: 
                self.res=root.val
            recur(root.left)
        
        recur(root)
        return self.res
