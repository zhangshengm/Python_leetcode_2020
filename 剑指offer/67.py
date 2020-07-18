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
