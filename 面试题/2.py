# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r1,r2="",""
        while l1:
              r1+=''.join(str(l1.val))
              l1=l1.next
        while l2:
              r2+=''.join(str(l2.val))
              l2=l2.next
        t=int(r1[::-1])+int(r2[::-1])
        t=str(t)
        a,i=ListNode(0),len(t)-1
        b=a
        while i>=0:
              b.next=ListNode(int(t[i]))
              b=b.next
              i-=1
        return a.next
              
  
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=ListNode(0)
        #flag代表进位值
        flag,b=0,a
        #当l1,l2都为None,flag=0时跳出循环
        while l1 or l2 or flag:
              #代表新的节点值
              t=(l1.val if l1 else 0) + (l2.val if l2 else 0)+flag
              #t大于10保留个位值，flag置为1
              if t>=10:
                 t-=10
                 flag=1
              #小于10,flag置为0
              else:
                  flag=0
              b.next=ListNode(t)
              b=b.next
              l1= l1.next if l1 else None
              l2=l2.next if l2 else None
        return a.next
