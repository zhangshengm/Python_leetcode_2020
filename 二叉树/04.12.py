# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        #由于有负值，同一个出发的节点可能有多条路径
        def DFS(root,tmp):
            if tmp==sum:
                self.flag+=1
            if not root: return 
            if root.left:
               DFS(root.left,tmp+root.left.val)
            if root.right:
               DFS(root.right,tmp+root.right.val) 
          
        if not root: return 0
        tmp=[root]
        self.flag=0
        while tmp:
              t=[]
              for node in tmp:
                  DFS(node,node.val) 
                  if node.left:
                      t.append(node.left)
                  if node.right:
                       t.append(node.right)    
              tmp=t
        return self.flag   
