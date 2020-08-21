# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #从后面往前面逆推
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or head.next==None:
           return head
        first=head
        second=head.next
        #第一个节点指向第三个节点及其之后的节点
        first.next=self.swapPairs(second.next)
        #第二个节点指向第一个节点
        second.next=first
        return second
