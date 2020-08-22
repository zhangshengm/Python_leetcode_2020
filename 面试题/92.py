# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        #start是节点编号,h为节点
        def DFS(start,h):
            if start==n: return h
            nextnode=DFS(start+1,h.next)
            h.next.next=h
            h.next=None
            return nextnode
        a=ListNode(-1)
        a.next=head
        b,after=a,a
        #before为m的前一个节点
        #b为m对应的节点
        for i in range(n+1):
            after=after.next
            if i<m:
               before=b
               b=b.next
        #翻转部分的节点
        reverse=DFS(m,b)
        before.next=reverse
        tmp,flag2=a,n
        while flag2>0:
              tmp=tmp.next
              flag2-=1
        tmp.next=after
        return a.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        a=ListNode(-1)
        a.next=head
        #before为m-1个节点
        b=a
        for i in range(m):
            before=b
            b=b.next
        # #此时b为m对应的节点
        tmp=b
        node1,after=None,None
        for j in range(n-m+1):
            #下一个节点
            after=tmp.next
            #当前节点指向上一个节点
            tmp.next=node1
            #上一个节点等于当前节点
            node1=tmp
            #当前节点等于下一个节点
            tmp=after
        before.next=node1
        b.next=after
        return a.next
