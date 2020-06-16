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
