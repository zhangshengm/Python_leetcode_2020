class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #建立伪节点
        a=ListNode(0)
        #右(左)边保存头节点，左(右)边遍历
        b=a
        while l1 and l2:
              if l1.val >l2.val:
                  a.next,l2=l2,l2.next
              else:
                  a.next,l1=l1,l1.next
              a=a.next
        #最后会有一个节点的值为空，另一个节点非空
        a.next=l1 if l1 else l2
        return b.next
