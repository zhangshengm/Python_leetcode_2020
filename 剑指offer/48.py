class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1: return len(s)
        #子串必须是连续的
        #保存连续子串的最大长度
        res=[]
        #保存子串的每个字符
        for i in range(len(s)-1):
            maxs=set()
            for j in range(i,len(s)):
               if s[j] not in maxs:
                  maxs.add(s[j])
               else:
                  break
               if not res or res[-1]<len(maxs):
                  res.append(len(maxs))
        return res[-1]
