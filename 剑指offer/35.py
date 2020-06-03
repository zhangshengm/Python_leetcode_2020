"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import deque
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def bfs(head):
            if not head: return None
            #新建节点
            copy=Node(head.val,None,None)
            #保存的是原始节点
            qu=deque()
            qu.append(head)
            Build[head]=copy
            while qu:
                 #每次出栈一个节点
                  temp=qu.pop()
                  if temp.next and temp.next not in Build: 
                     qu.append(temp.next)
                     Build[temp.next]=Node(temp.next.val,None,None)
                  if temp.random and temp.random not in Build: 
                     qu.append(temp.random)
                     Build[temp.random]=Node(temp.random.val,None,None)
                  #dict get()根据键返回值，如果键不存在，返回空
                  #temp非空，但temp.next和temp.random不一定
                  Build[temp].next=Build.get(temp.next)
                  Build[temp].random=Build.get(temp.random)
            return copy
        Build={}
        return bfs(head)
        
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def dfs(head):
            if not head: return None
            if head in Build:
               return Build[head]
            #新建节点
            node=Node(head.val,None,None)
            #保存节点
            Build[head]=node
            node.next=dfs(head.next)
            node.random=dfs(head.random)
            return node
        Build={}
        return dfs(head)
    
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        def clonenode(head):
            if not head: return None
            if head in Build:
                return Build[head]
            else:
                t=Node(head.val,None,None)
                Build[head]=t
                return  Build[head]
        if not head: return head
        Build,node={},head
        n=Node(head.val,None,None)
        Build[node]=n
        while node:
              Build[node].next=clonenode(node.next)
              Build[node].random=clonenode(node.random)
              node=node.next
        return n
