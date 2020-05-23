class Solution:
    def replaceSpace(self, s: str) -> str:
        s1=[]
        i=0
        while i <len(s):
            if s[i].isspace():
               s1.append('%20')
            else:
                s1.append(s[i])
            i+=1
        return ''.join(s1)
    
class Solution:
    def replaceSpace(self, s: str) -> str:
        return ''.join('%20' if c==' ' else c for c in s)

class Solution:
    def replaceSpace(self, s: str) -> str:
       s1=[]
       for i in s:
            if i==' ':
                s1.append('%20')
            else:
                s1.append(i)
       return ''.join(s1)

class Solution:
    def replaceSpace(self, s: str) -> str:
       s1=''
       for i in s:
            if i==' ':
                s1+='%20'
            else:
                s1+=i
       return s1
