
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        flag,First=0,head
        if not head: return head
        #如果删除的是头节点
        if val==head.val:
            First=First.next
            return First
        #保存头结点
        t=First
        while First:
              before=First
              after=First.next
              #删除节点
              if val==after.val:
                 before.next=after.next
                 return t
              First=First.next
              #保存首节点
              if flag==0:
                  t.next=after
                  flag=1
