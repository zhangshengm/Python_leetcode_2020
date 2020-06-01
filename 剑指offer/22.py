# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#遍历所有节点，耗时最长
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        flag,s1=0,[]
        if not head: return None
        while head:
              s1.append(head)
              head=head.next
              flag+=1
        before=s1[flag-k]
        
 #建立双指针
 class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        before,after=head,head
        #使得两个指针间距节点为k
        for i in range(k):
            after=after.next
        #当after指向空时，before指到倒数第k个节点
        while after!=None:
            before,after=before.next,after.next
        return before
 
