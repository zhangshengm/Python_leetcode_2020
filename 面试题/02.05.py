
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

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp=0
        res=""
        while l1 or l2:
            if l1: 
                t1=l1.val
                l1=l1.next
            else: t1=0
            if l2: 
                t2=l2.val
                l2=l2.next
            else: t2=0
            s=t1+t2+tmp
            if s>=10:
               s-=10
               tmp=1
            else:
               tmp=0
            res+=''.join(str(s))
            if not l1 and not l2 and tmp==1:
               res+=''.join(str(1))            
        flag=0
        node=ListNode(int(res[flag]))
        first=node
        flag+=1
        while flag<len(res):
              node2=ListNode(int(res[flag]))
              node.next=node2
              node=node2
              flag+=1
        return first
