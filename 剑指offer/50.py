class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s: return " "
        hashmap={}
        i=0
        while i<len(s):
            if s[i] not in hashmap:
                hashmap[s[i]]=1
            else:
                hashmap[s[i]]+=1
            i+=1
        #如果出现次数为1的字符存在
        if 1 in hashmap.values():
           #index返回第一个匹配项
           res=list(hashmap.keys())[list(hashmap.values()).index(1)]
        else:
            return " "
        return res

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s: return ' '
        h={}
        for i in s:
            #如果新加的字符不在字典里，值为True；如果重复，值为false
            h[i]=i not in h
        for k,v in h.items():
            if v: return k
        return ' '
