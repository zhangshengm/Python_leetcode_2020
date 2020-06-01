# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        flag,s1=0,[]
        if not head: return head
        while head:
              s1.append(head)
              head=head.next
        #t取最后一个节点
        t=s1[-1]
        while s1:
            node=s1.pop()
            #最后一个节点指向空
            if len(s1)==0:  node.next=None
            #其余节点指向下一个节点
            else:   node.next=s1[-1]
            ##建立链接关系之后，再保存第一个节点
            if flag==0: 
                t.next=node.next
                flag=1
        return t
#递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(before,now):
            #before为尾结点
            if now==None: return before
            #保存下一个节点
            node=now.next
            #改变当前节点链接
            now.next=before
            return helper(now,node)
        return helper(None,head)
    
#建立双指针，一边遍历，一边链接
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        cur=head
        pre=None
        while cur:
            #新建一个节点
            temp=ListNode(cur.val)
            #建立指向关系
            temp.next=pre
            pre=temp
            cur=cur.next
        return temp
