# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    #反转链表: 两个参数，一个代表上一个节点,另一个代表当前节点；当当前节点为空时，返回上一个节点
    def reverseList(self, head: ListNode) -> ListNode:
        #上一个节点和当前节点
        def helper(before,now):
            if not now: return before
            tmp=now.next
            now.next=before
            return helper(now,tmp)
        return helper(None,head)
     
     
    #两个链表的第一个公共节点: 两个节点依次遍历，相等则跳出循环（找到相同节点或者同时为空），当其中一个链表遍历完，让它指向另一个链表的原始链表。
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1,node2=headA,headB
        while node1!=node2:
            if node1:
                node1=node1.next
            else:
                node1=headB
            if node2:
                node2=node2.next
            else:
                node2=headA
        return node1
