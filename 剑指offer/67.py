class Solution:
    def strToInt(self, str: str) -> int:
        if not str: return 0
        f,tmp,flag=0,"",2**31
        num= ['0','1','2','3','4','5','6','7','8','9']
        l,r=-flag,flag-1
        while f<len(str):
            if str[f]==' ':
                f+=1
            else:break
        #f为第一个非空字符的下标,如果全为空字符
        if f==len(str): return 0

        #第一个非空字符是整数
        if str[f] in num:
             t=f+1
             while  t<len(str) and str[t] in num:
                   t+=1
             #符号后有整数
             tmp=str[f:t]

   
        #是正负号
        elif str[f] in ['-','+']:
             t=f+1
             while t<len(str) and str[t] in num:
                   t+=1
             #符号后有整数
             if t-f>1:
                 tmp=str[f:t]
             else:
                 return 0

        #第一个非空字符不是加减号或者数字
        else:
            return 0
                
        #判断正数范围
        if int(tmp)>r:
            return r
        elif int(tmp)<l:
            return l
        else:
            return int(tmp)
        
class Solution:
    def strToInt(self, str: str) -> int:
        #返回计算值，如果越界则返回最大值或最小值
        def sums(s,sign):
            res=0
            t=len(s)-1
            while t>=0:
                res+=(ord(s[len(s)-1-t])-ord('0'))*(10**(t))
                t-=1
                if sign==1:
                   if res >self.r:
                     return self.r
                else:
                   if -res <self.l:
                      return self.l
            return res if sign==1 else -res
                  
        tmp,flag="",2**31
        self.l,self.r=-flag,flag-1
        #f为下标位置,sign为符号位
        final,sign,t=0,1,1
        #删除首尾空格字符
        str=str.strip()
        #如果全为空格
        if not str: return 0
        #如果第一个非空字符是加减号
        if str[0] in ['+','-']:
           if str[0]=='+':
               sign=1
           else:
               sign=-1
           t=1
           while t<len(str) and '0'<=str[t] <='9':
                    t+=1
           #如果符号位后是整数
           if t>1:
              tmp=str[1:t]
           #如果符号位后是整数
           else:
              return 0

        elif  '0'<=str[0]<='9':
              t=1
              while t<len(str) and '0'<=str[t]<='9':
                    t+=1
              tmp=str[0:t]

        #如果第一个非空字符不是数字或者加减号
        else:
            return 0
        final=sums(tmp,sign)
        return final

class Solution:
    def strToInt(self, str: str) -> int:
        #判断是否超出界限
        def maxminv(n,sign):
            if sign==1:
                if  n>self.r:
                    return False
            else:
                if -n<self.l:
                    return False
            return True

        flag=2**31
        self.l,self.r=-flag,flag-1
        #f为下标位置,sign为符号位
        final,sign=0,1
        res=0
        #删除首尾空格字符
        str=str.strip()
        #如果全为空格
        if not str: return 0
        #如果第一个非空字符是加减号
        if str[0] in ['+','-']:
           if str[0]=='+': sign=1
           else: sign=-1
           t=1
           while t<len(str) and '0'<=str[t] <='9':
                 res=res*10+(ord(str[t])-ord('0'))
                 if not maxminv(res,sign):
                    return self.r if sign==1 else self.l
                 t+=1
           #如果只有符号位
           if res==0: return 0   
        

        elif  '0'<=str[0]<='9':
              t=0
              while t<len(str) and '0'<=str[t]<='9':
                  res=res*10+(ord(str[t])-ord('0'))
                  if not maxminv(res,sign):
                    return self.r if sign==1 else self.l
                  t+=1
            
        #如果第一个非空字符不是数字或者加减号
        else:
            return 0
        
        return sign*res
