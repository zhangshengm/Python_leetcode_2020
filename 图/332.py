#通过图中所有边恰好一次且行遍所有顶点的通路称为欧拉通路。
#通过图中所有边恰好一次且行遍所有顶点的回路称为欧拉回路。
#具有欧拉回路的无向图称为欧拉图。
#具有欧拉通路但不具有欧拉回路的无向图称为半欧拉图。

#对于无向图G，G是欧拉图当且仅当G是连通的且没有奇度顶点。
#对于无向图G，G是半欧拉图当且仅当G是连通的且G中恰有2个奇度顶点。
#对于有向图 G，G 是欧拉图当且仅当 G的所有顶点属于同一个强连通分量且每个顶点的入度和出度相同。
#对于有向图 G，G是半欧拉图当且仅当 G 的所有顶点属于同一个强连通分量且
#  恰有一个顶点的出度与入度差为 1；
#  恰有一个顶点的入度与出度差为 1；
#  所有其他顶点的入度和出度相同.
  
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def DFS(k):
            while vec[k]:
                  tmp=heapq.heappop(vec[k])
                  DFS(tmp)
            res.append(k)
        vec=defaultdict(list)
        for start,end in tickets:
            vec[start].append(end)
        # print(vec)
        for k in vec:
            heapq.heapify(vec[k])
        res=[]
        DFS("JFK")
        return res[::-1]
