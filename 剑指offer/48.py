class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1: return len(s)
        #子串必须是连续的
        #保存连续子串的最大长度
        res=[]
        for i in range(len(s)-1):
            #保存子串的每个字符
            maxs=set()
            for j in range(i,len(s)):
               if s[j] not in maxs:
                  maxs.add(s[j])
               else:
                  break
               if not res or res[-1]<len(maxs):
                  res.append(len(maxs))
        return res[-1]
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        #子串必须是连续的
        #保存连续子串的最大长度
        res=1
        #保存子串的每个字符
        for i in range(len(s)-1):
            maxs=set()
            for j in range(i,len(s)):

               if s[j] not in maxs:
                  maxs.add(s[j])
               else:
                  break
               res=max(res,len(maxs))
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1: return len(s)
        head,res=0,1
        #保存某个元素最近出现的位置
        hashmap={}
        for i in range(len(s)):
            #如果元素重复，更新头部指针指向首个重复元素的后一个元素
            #max(head,hashmap[s[i]]+1)保证head一直往后
            if s[i] in hashmap:
                head=max(head,hashmap[s[i]]+1)
            #    head=max(hashmap[s[i]],head)

            #更新当前字符最近出现的位置，当前坐标为i
            hashmap[s[i]]=i

            #从第head个字符到第i个字符均为不重复子串
            res=max(res,i-head+1)
        return res
