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
        
        
class Solution:
    def isUgly(self, num: int) -> bool:
        t=[2,3,5]
        #判断能否被2,3,5整除
        def divide_t(n): 
           for i in range(len(t)):
               if n%t[i]==0:
                  return True
           return False
        #如果大于1，且能被整除
        while num>1 and divide_t(num):
            for i in range(len(t)):
                if num%t[i]==0:
                   num=num/t[i]
        return num==1
