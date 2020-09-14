class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

def create_node(num):
    if not num: return num
    visited={}
    clone_node=Node(0,[])
    visited[0]=clone_node
    target=clone_node
    for i in range(len(num)):
        if i in visited:
           clone_node=visited[i]
        else:
            clone_node=Node(i,)
            visited[i]=clone_node

        for nei in num[i]:
                if nei in visited:
                   tmp_node=visited[nei]
                else:
                   tmp_node=Node(nei,[])
                   visited[nei]=tmp_node
                clone_node.neighbors.append(tmp_node)              
    return target
