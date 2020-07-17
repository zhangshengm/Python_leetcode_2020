
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
    return s[n:]+s[:n]

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res=[]
        for i in range(n,len(s)):
            res.append(s[i])
        for j in range(0,n):
             res.append(s[j])
        return "".join(res)
        
