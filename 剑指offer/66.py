class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        #B[i]缺A[i]的乘数因子,从少到多计算，简化运算过程
        tmp,B=1,[1]*len(a)
        #从第二个元素开始
        for i in range(1,len(a)):
            B[i]=B[i-1]*a[i-1]
        #从倒数第二个元素开始:
        for j in range(len(a)-2,-1,-1):
            tmp*=a[j+1]
            B[j]*=tmp
        return B
        
