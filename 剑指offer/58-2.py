
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
    return s[n:]+s[:n]

#join函数列表转list
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res=[]
        for i in range(n,len(s)):
            res.append(s[i])
        for j in range(0,n):
             res.append(s[j])
        return "".join(res)
        
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res=[]
        for i in range(n,n+len(s)):
            res.append(s[i%len(s)])
          
        return "".join(res)
        
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res=""
        for i in range(n,n+len(s)):
            res+=s[i%len(s)]
          
        return res
        
        
