class Solution:
    def isHappy(self, n: int) -> bool:
        def intlist(num):
            res=[]
            while num:
                tmp=num%10
                res.append(tmp)
                num//=10
            return res
        def compute_sum(num):
            tmp=0
            for i in num:
                tmp+=i**(2)
            return tmp
        t2=0
        h=set()
        while t2!=1:
             t1=intlist(n)
             t2=compute_sum(t1)
             if t2 not in h:
                h.add(t2)
             else:
                return False
             if t2==1:
                return True
             n=t2
