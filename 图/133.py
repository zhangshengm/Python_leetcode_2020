"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited={}

        def DFS(node):
            #空节点就返回
            if not node: return node
            #如果该节点之前已经克隆过了，返回克隆的节点即可
            if node in self.visited:
                return self.visited[node]
            #克隆目标节点
            clone_node=Node(node.val,[])
            #将克隆的节点指向目标节点
            self.visited[node]=clone_node
            #克隆邻居
            if node.neighbors:
               clone_node.neighbors=[DFS(i) for i in node.neighbors]
            return clone_node 
        return DFS(node)
        
        

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        self.visited={}
        tmp=[node]
        clone_node=Node(node.val,[])
        self.visited[node]=clone_node
        target=clone_node
        while tmp:
              t=[]
              for n in tmp:
                #待克隆的节点
                clone_node=self.visited[n]
 
                #克隆邻居
                for no in n.neighbors: 
                  #如果邻居节点已经克隆过，直接加入邻居集合即可
                  if no in self.visited:
                     clone_node.neighbors.append(self.visited[no])
                  #如果邻居节点没有克隆过，克隆即可
                  else:
                     t.append(no)
                     tmp_node=Node(no.val,[])
                     clone_node.neighbors.append(tmp_node)
                     self.visited[no]=tmp_node
              tmp=t
        return target
