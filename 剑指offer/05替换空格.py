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
