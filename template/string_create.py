
class Solution:
    #最长回文字符串,babad返回 bab或者aba
    def longestPalindrome(self, s: str) -> str:
       if not s: return ""
       dp=[[False]*len(s) for _ in range(len(s))]
       dp[0][0]=True
       start,tmp=0,1
       for i in range(1,len(s)):
           for j in range(i-1,-1,-1):
               if s[i]==s[j]:
                   if i-j<=2:
                       dp[j][i]=True
                   else:
                       dp[j][i]=dp[j+1][i-1]
               if dp[j][i]:
                  if i-j+1>tmp:
                     tmp=i-j+1
                     start=j
       return s[start:start+tmp]
    
    #统计有多少个回文子串,不同位置开始都算
    def countSubstrings(self, s: str) -> int:
       if not s: return 0
       dp=[[False]*len(s) for _ in range(len(s))]
       dp[0][0]=True
       count=0
       for i in range(len(s)):
           for j in range(i,-1,-1):
               length=i-j
               #如果字符长度等于0
               if length==0:
                   count+=1
                   dp[j][i]=True
               #长度等于1或2，看两个字符是否相等
               elif length==1 or length==2:
                   if s[i]==s[j]:
                      count+=1
                      dp[j][i]=True
               else:
                   if s[i]==s[j]:
                      dp[j][i]=dp[j+1][i-1]
                      if dp[j][i]:
                         count+=1
       return count

    #无重复字符的最长子串,指针法
    def lengthOfLongestSubstring(self, s: str) -> int:
       if not s: return 0
       i,h=1,set()
       h.add(s[0])
       start,res=0,[1]
       while i<len(s):
            #如果不重复，将字符加入h中，判断下一个字符
            if s[i] not in h:
               h.add(s[i])
               i+=1
            #如果重复，把现在不重复的子串长度放到res中
            #h删除start对应的字符，start后移一位
            else:
               res.append(i-start)
               h.remove(s[start])
               start+=1
       #保留最后一次判断的不重复子串
       res.append(i-start)
       return max(res)
