class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #空树是一颗平衡二叉树
        if not root: return True
        s1=[root]
        #返回某个节点的树的最大深度
        def maxdeep(root):
            if not root: return 0
            return max(maxdeep(root.left),maxdeep(root.right))+1
        #循环判断每个节点的左右子树
        while s1:
              t=[]
              for node in s1:
                 a,b=0,0
                 if node.left:
                    a=maxdeep(node.left)
                    t.append(node.left)
                 if node.right:
                    b=maxdeep(node.right)
                    t.append(node.right)
                 if abs(a-b)>=2:
                    return False
              s1=t
        return True
