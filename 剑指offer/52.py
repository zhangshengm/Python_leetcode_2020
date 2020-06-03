# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s1=set()
        if not (A or B): return None
        #遍历第一个链表
        while headA:
              s1.add(headA)
              headA=headA.next
        t=len(s1)
        #遍历第二个链表，加入集合中
        while headB:
              s1.add(headB)
              #如果是公共节点，长度不会变化
              if t==len(s1):
                  return headB
              else:
                  t=t+1
              headB=headB.next
        return None
        
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not (headB or headB): return None
        a=set()
        b=set()
        while headA or headB:
              if headA:
                 if headA in b:
                    return headA
                 else:
                    a.add(headA)
                    headA=headA.next
                 
              if headB:
                 if headB in a:
                    return headB
                 else:
                    b.add(headB)
                    headB=headB.next
        return None
        
  class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        #当两个链表均遍历完后指向None,相等跳出循环
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1
