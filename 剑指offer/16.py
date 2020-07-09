class Solution:
    def myPow(self, x: float, n: int) -> float:

        t=-n if n<0 else n
        #保存奇数次方多余
        res=1
        while t:
            # t&1 
            if t%2==1:
               res*=x
            x*=x
            # t>>=1,向右移动一位，删除最后一位
            t//=2
        return res if n>0 else 1/res
