class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None:
           return head
        def DFS(tail,h):
            if h==None: return tail
            #先保存当前节点的下一个节点
            tmp=h.next
            #当前节点指向上一个节点
            h.next=tail
            return DFS(h,tmp)
        return DFS(None,head)
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res=[]
        #保存所有节点的值
        while head:
            res.append(head.val)
            head=head.next
        a=ListNode(0)
        c=a
        while res:
              b=ListNode(res.pop())
              c.next=b
              c=c.next
        c.next=None
        return a.next
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head.next:
           return head
        #找到最后一个非空节点，并返回
        nextnode=self.reverseList(head.next)
        #每次递归找到当前节点和上一个节点。当前节点指向上一个节点
        head.next.next=head
        #上一个节点指向空
        head.next=None
        return nextnode
