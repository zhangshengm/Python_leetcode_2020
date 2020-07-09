class Solution:
    def printNumbers(self, n: int) -> List[int]:
        t,res=10,1
        while n:
             if n%2==1:
                res*=t
             t*=t
             n>>=1
        return list(range(1,res))
