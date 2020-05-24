class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        #转换为字符数组
        s1=sentence.strip()
        s1=s1.split(' ')
        i=0
        while i<len(s1):
              #原单词长度小于搜索单词
              t=s1[i]
              len1=len(searchWord)
              if len(s1[i])< len1:
                 i+=1
                 continue
              #遍历搜索单词
              for j in range(len1):
                    if searchWord[j]!=t[j]:
                        # i+=1
                        break
                    if j==(len1-1):
                        return i+1
              i+=1
        return -1
        
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        #转换为字符数组
        s1=sentence.strip()
        s1=s1.split(' ')
        # k=1
        len1=len(searchWord)
        for k,i in enumerate(s1):
              #原单词长度小于搜索单词
              if len(i)< len1:
                 continue
              #遍历搜索单词
              for j in range(len1):
                    if searchWord[j]!=i[j]: 
                        break
                    if j==len1-1:
                        return k+1

        return -1
