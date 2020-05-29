# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        flag,s1=0,[]
        if not head: return head
        while head:
              s1.append(head)
              head=head.next
        #t取最后一个节点
        t=s1[-1]
        while s1:
            node=s1.pop()
            #最后一个节点指向空
            if len(s1)==0:  node.next=None
            #其余节点指向下一个节点
            else:   node.next=s1[-1]
            #保存第一个节点
            if flag==0: 
                t.next=node.next
                flag=1
        return t
