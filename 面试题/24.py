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

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new=ListNode(0)
        new.next=head
        pre=new
        #head不为最后一个非空节点,循环
        while head and head.next:
              #找到第一个和第二个节点
              first=head
              second=head.next
              
              #指向交换后的第一个节点
              pre.next=second
              #保存第三个节点
              first.next=second.next
              #第二个节点指向第一个节点
              second.next=first

              pre=first
              head=first.next
        return new.next     
