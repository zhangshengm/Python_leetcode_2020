class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder: return True
        #找到根节点
        root=postorder[-1]
        len_list=len(postorder)
        i=0
        #找到第一个大于根节点的值,划分左右子树
        for i in range(len_list):
            if postorder[i] >root:
                break
        #没有大的元素,不执行右子树操作
        if i==len_list-1:
            t=len_list-1
        #从第i个元素执行右子树操作
        else:
            t=i
        #如果右子树中有小于根节点的值，则不成立
        for j in range(t,len_list-1):
            if postorder[j]<root:
                return False
        f_left,f_right=True,True
        #左子树非空进行判断
        if t >0:
           f_left=self.verifyPostorder(postorder[0:t])
        if len_list-1>t:
           f_right=self.verifyPostorder(postorder[t:len_list-1])

        return f_left and f_right
