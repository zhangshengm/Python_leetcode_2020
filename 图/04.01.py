
    #构造有向的邻接矩阵，L[node]=[邻接节点]
    #首先考虑自环情况，自环情况仅影响start=end情况，然后删除自环的节点
    #广度优先遍历res=L[start]，查看target是否在res中，不在则pop出节点t，res新加入L[t]继续判断
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        L=[[] for _ in range(n)]
        for i in range(len(graph)):
            if graph[i][1] not in L[graph[i][0]]:
               L[graph[i][0]].append(graph[i][1])
        flag=False
        res=[]
        for node in L[start]:
            res.append(node)
        h=set()
        h.add(start)
        while res:
              if target in res:
                 flag=True
                 break
              else:
                  t=res.pop()
                  for node in L[t]:
                    if node not in h:
                       res.append(node)
                       h.add(node)      
        return flag
