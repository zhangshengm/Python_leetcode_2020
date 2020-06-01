
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
#双指针遍历
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        #如果是首节点，返回之后的节点
        if head.val == val: return head.next
        #第一个节点和第二个节点
        pre, cur = head, head.next
        #找到删除的节点
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        #删除该节点
        if cur: pre.next = cur.next
        return head
