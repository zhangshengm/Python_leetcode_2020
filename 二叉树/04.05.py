class Solution:
    #将每个元素按序添加到数组中，判断当前元素是否小于前一个元素
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        def DFS(root):
            if not root:
               return [] 
            return DFS(root.left)+[root.val]+DFS(root.right)
        s=DFS(root)
        for i in range(1,len(s)):
            if s[i]<=s[i-1]:
                return False
        return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        nums=[]
        pre=float('-inf')
        while nums or root:
               #先保存所有的左节点[2,1]
               while root:
                  nums.append(root)
                  root=root.left
               root=nums.pop()
               if root.val<=pre:
                   return False
               #当前节点值变成前一个节点的值
               pre=root.val
               #如果当前节点有右节点，当前节点变为右节点；如果没有root=None,循环为下一个左节点
               root=root.right
        return True
        
