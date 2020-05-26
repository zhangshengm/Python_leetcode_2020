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
        # s1.append([root.val])
        s2=[root]
        while s2:
              #存每一层的节点
              t=[]
              t1=[]
              #遍历每一层节点
              for node in s2:
                 t1.append(node.val)
                 if node.left: 
                    t.append(node.left)
                 if node.right:
                    t.append(node.right)
              s1.append(t1)
              s2=t
        return s1

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
      
        s1=[]
        #如果树为空，返回空列表
        if not root: return s1
        #注意考虑节点和节点的值得区别
        s2=deque()
        s2.append(root)
        while s2:
            t2=[]
            num=len(s2)
            for i in range(num):
               node=s2.popleft()
               t2.append(node.val)
               if node.left: 
                  s2.append(node.left)
               if node.right: 
                  s2.append(node.right)
            s1.append(t2)
        return s1
