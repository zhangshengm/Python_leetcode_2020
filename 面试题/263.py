class Solution:
    #判断是否为丑数可以考虑辗转相除法
    def isUgly(self, num: int) -> bool:
        while num>1 and (num%2==0 or num%3==0 or num%5==0):
             if num%2==0:
                 num=num/2
             if num%3==0:
                 num=num/3
             if num%5==0:
                 num=num/5
        return num==1
        
        
