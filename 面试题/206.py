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
