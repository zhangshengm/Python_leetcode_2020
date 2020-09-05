class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        #求最大公约数
        def gcd(a,b):
            if a%b==0:
                return b
            else:
                return gcd(b,a%b)
        #思路是先确定第n个丑数的取值范围是在[min(a,b,c),n*min(a,b,c)],确定low,high
        #mid=（low+high）//2
        #计算每个mid数的丑数个数，判断是否和n相等
        a,b,c=sorted([a,b,c])
        x_ab=a*b/gcd(a,b)
        x_ac=a*c/gcd(a,c)
        x_bc=b*c/gcd(b,c)
        x_abc=x_ab*c/gcd(x_ab,c)
        low,high=a,n*a
        if a==1:
            return n
        while low<=high:
            mid=(high+low)//2
            num=mid//a+mid//b+mid//c-mid//x_ab-mid//x_ac-mid//x_bc+mid//x_abc
            if num<n:
                 low=mid+1
            else:
                 high=mid-1
        return low
        
