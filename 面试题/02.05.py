
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1,s2="",""
        while l1:
              s1+=''.join(str(l1.val))
              l1=l1.next
        while l2:
              s2+=''.join(str(l2.val))
              l2=l2.next
        tmp=int(s1[::-1])+int(s2[::-1])
        tmp=str(tmp)
        t=len(tmp)-1
        first=ListNode(int(tmp[t]))
        t,second=t-1,first
        while t>=0:
              node=ListNode(int(tmp[t]))
              second.next=node
              second=second.next
              t-=1
        return first
