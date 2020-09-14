class Solution:

    #深度优先会超时
    def ladderLength(self, beginWord, endWord, wordList):
       
        self.end=endWord
        self.res=[]
        #计算单词与列表中单词的不相同的字母个数
        def k_length(source,wo):
            tmp=[0]*len(wo)
            for w1 in range(len(wo)):
                flag=0
                for i in range(len(source)):
                    if source[i]!=wo[w1][i]:
                        flag+=1
                tmp[w1]=flag
            return tmp


        def DFS(path,word):
            if path[-1]==self.end:
               self.res.append(len(path))

            tmp=k_length(path[-1],word)
            for i in range(len(tmp)):
                if tmp[i]==1:
                   DFS(path+[word[i]],word[:i]+word[i+1:])           
            
        if endWord not in wordList:
            return 0
        if beginWord in wordList:
            wordList.remove(beginWord)
        DFS([beginWord],wordList)

        return min(self.res) if self.res else 0
        

class Solution:
     #广度优先遍历，下一层的目标词语是上一层词语相差一个单词的词语，每次记得从字典中删除走过的单词
    def ladderLength(self, beginWord, endWord, wordList):
        tmp=[beginWord]
        depth=1
        wordList=set(wordList)
        while tmp:
            t=[]
            for word in tmp:
                if word==endWord:
                    return depth
                for i in range(len(word)):
                    for indice in "abcdefghijklmnopqrstuvwxyz":
                        new_word=word[:i]+indice+word[i+1:]
                        if new_word in wordList:
                            t.append(new_word)
                            wordList.remove(new_word)
            tmp=t
            depth+=1
        return 0
