# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        s1=[]
        #如果树为空，返回空列表
        if not root: return s1
        #注意考虑节点和节点的值得区别
        s1.append([root.val])
        s2=[root]
        flag=1
        while s2:
              #存每一层的节点
              t=[]
              t1=[]
              flag+=1
              #遍历每一层节点
              for node in s2:
                   if node.left: 
                     t.append(node.left)
                     t1.append(node.left.val)
                   if node.right:
                     t.append(node.right)
                     t1.append(node.right.val)
              if t1 and flag%2==0:
                 t1.reverse()
                 s1.append(t1)
              if t1 and flag%2==1:
                 s1.append(t1)
              s2=t
        return s1
