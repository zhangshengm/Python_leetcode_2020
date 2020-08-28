class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        target=24
        error=1e-6
        # +,*,-,/
        f1,f2,f3,f4=0,1,2,3
        def DFS(num):
            if not num:
               return False
            if len(num)==1:
               return abs(num[0]-target)<error
            #可能有重复值，用下标选择不同的元素
            for i,i_x in enumerate(num):
                for j,j_x in enumerate(num):
                    #任选两个数字A(4,2)=4!/(4-2)!
                    if i!=j:
                       new_num=[]
                       #将剩余元素放到新的list中
                       for k,k_x in enumerate(num):
                           if k!=i and k!=j:
                              new_num.append(k_x)
                       for m in range(4):
                           #加法和乘法运算，满足交换律
                           #i=0,j=1,2,3   [0,1] [0,2] [0,3]
                           #i=1,j=0,1,2   [1,0] [1,2] [1,3]
                           #i=2,j=0,1,3   [2,0] [2,1] [2,3]
                           #i=3,j=0,1,2   [3,0] [3,1] [3,2]
                           if m<=1 and i>j:
                              continue
                           if m==f1:
                              new_num.append(i_x+j_x)
                           elif m==f2:
                              new_num.append(i_x*j_x)
                           elif m==f3:
                               new_num.append(i_x-j_x)
                           elif m==f4:
                               if j_x==0:
                                  continue
                               else:
                                  new_num.append(i_x/j_x)
                           if DFS(new_num):
                              return True
                           #将新加入的元素移除，重新考虑下个运算
                           new_num.pop()
            return False
        return DFS(nums)
