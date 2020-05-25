class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        #如果输入空子树，返回不是
        result=False
        if not A or not B:
            return False
        if A.val==B.val:
            #递归判断当前节点下,B是否为A的子树
            result=self.dfs(A,B) 
        if not result:
            #判断B是否在A的左子树里面
            result=self.isSubStructure(A.left,B)
        if not result:
            #判断B是否在A的右子树里面
            result=self.isSubStructure(A.right,B)
        
        return result
    
    def dfs(self, A: TreeNode, B: TreeNode) -> bool:
        #如果跳过了B的最后一个节点，是子树
        if B == None:
            return True
        #如果A子树为空了，不是子树
        if A == None:
            return False
        #如果值不相等，不是子树
        if A.val !=B.val:
            return False
        return self.dfs(A.left,B.left) and self.dfs(A.right,B.right)
