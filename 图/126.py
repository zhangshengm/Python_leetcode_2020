class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        wordList=set(wordList)
        dic=collections.defaultdict(list)
        L=len(beginWord)
        #建立字典中的映射关系,h*t=[hot],do*=[dot],lo*=[lot,log]
        for w in wordList:
            for i in range(L):
                dic[w[:i]+"*"+w[i+1:]].append(w)

        q,s=collections.deque([(beginWord,[beginWord])]),collections.deque()
        #保存走过的节点，和路径
        seen,res=set(),[]
        while q:
            while q:
                w,path=q.popleft()
                if w==endWord: res.append(path)
                #当节点出栈时，记录走过的节点
                seen.add(w)
                #寻找相差1的节点
                for i in range(L):
                    tmp=dic[w[:i]+"*"+w[i+1:]]
                    for tmp_word in tmp:
                        #下一层节点没有走过
                        if tmp_word not in seen:
                            s.append(([tmp_word,path+[tmp_word]]))
            #当某一层遍历完，res中有路径时，即为最短的
            if res: return res
            q,s=s,q     
       
        return []
