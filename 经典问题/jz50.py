class Solution:
    #python 3.5以前,dict插入无序，利用有序的字典
    #python 3.6以后，插入有序
    #判断字符是否重复出现，返回第一个不重复的字符
    def firstUniqChar(self, s: str) -> str:
         if not s: return " "
         d=collections.OrderedDict()
         for i in s:
                 d[i]= i not in d
      
         for k,v in d.items():
             if v:
                 return k
         return " "

        
class Solution:
    #记录字符出现的次数，返回第一个出现次数为1的字符
    def firstUniqChar(self, s: str) -> str:
         if not s: return " "
         d=collections.OrderedDict()
         for i in s:
             if i not in d:
                 d[i]=1
             else:
                 d[i]+=1
         for k,v in d.items():
             if v==1:
                 return k
         return " "
