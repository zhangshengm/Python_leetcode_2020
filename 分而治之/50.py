class Solution:
    #O(logn)
    #O(logn)
    def myPow(self, x: float, n: int) -> float:
        def quickpow(N):
            if N==0:
                return 1.0
            y=quickpow(N//2)

            return y*y if N%2==0 else y*y*x
     
        return quickpow(n) if n>0 else 1.0/quickpow(-n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0.0: return 0.0
        res=1
        if n<0: x,n=1/x,-n
        while n:
            #将奇数项的x乘到res项
            if n%2==1: res*=x
            x*=x
            n//=2
        return res
