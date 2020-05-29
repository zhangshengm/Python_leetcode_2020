# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        s1=[]
        while head:
            s1.append(head.val)
            head=head.next
        return s1[::-1]
        
from collections import deque
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
       s1=deque()
       while head:
           s1.appendleft(head.val)
           head=head.next
       return list(s1)
       
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return  self.reversePrint(head.next) +  [head.val] if head else []
