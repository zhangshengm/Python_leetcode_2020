class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph=[[float('inf') for _ in range(N+1)] for _ in range(N+1)]
        for u,v,w in times:
            graph[u][v]=w
        #源点到源点花费的时间为0
        graph[K][K]=0

        #除了源节点之外的其他节点
        unmark=list(range(N+1))
        unmark.remove(K)
        
        #[2] [1,3,4]
        for _ in range(1,N):
            min_time=float('inf')
            min_node=0
            for i in unmark:
                if graph[K][i]<min_time:
                   min_time=graph[K][i]
                   min_node=i
            unmark.remove(min_node)
            for j in unmark:
                graph[K][j]=min(graph[K][j],graph[K][min_node]+graph[min_node][j])

        max_value=-1
        for j in range(1,N+1):
            if j!=K:
                max_value=max(max_value,graph[K][j])
        return -1 if max_value==float('inf') else max_value
        
