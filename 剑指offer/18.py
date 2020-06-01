
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        flag,First,t=0,head,None
        if not head: return head
        #如果删除的是头节点
        if val==head.val:
            First=First.next
            return First
        t=First
        #遍历每个节点
        while First:
              #保存当前节点
              before=First
              #取到下一个节点
              after=First.next
              #删除节点
              if val==after.val:
                 after=after.next
                 before.next=after
                 return t
              #遍历节点
              First=First.next
              #保存首节点
              if flag==0:
                  t.next=after
                  flag=1
