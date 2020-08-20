# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:
           return l2
        elif l2==None:
           return l1
        elif l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2
            
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=ListNode(0)
        b=a
        while l1 and l2:
              if l1.val>l2.val:
                 b.next,l2=l2,l2.next
              else:
                 b.next,l1=l1,l1.next
              b=b.next
        b.next= l1 if l1 else l2
        return a.next
