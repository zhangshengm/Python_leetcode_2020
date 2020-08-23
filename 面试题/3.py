class Solution:
    #用start代表每个不重复子串的开头位置，i为字符重复的位置,i-start为不重复子串的长度
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
           return len(s)
        h=set()
        i,res,start=1,[],0
        h.add(s[0])
        while i<len(s):
              if s[i] not in h:
                 h.add(s[i])
                 i+=1
              else:
                 res.append(i-start)
                 h.remove(s[start])
                 start+=1
        res.append(i-start)
        return max(res)
