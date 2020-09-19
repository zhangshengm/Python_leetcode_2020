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
    
    
    #合并两个有序列表: 建立伪节点，如果都非空，则小的节点的值建立新节点，建立链接关系；如果有一个为空，则指向另一个非空链表
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        b=ListNode(-1)
        a=b
        while l1 and l2:
              if l1.val<=l2.val:
                 tmp=ListNode(l1.val)
                 l1=l1.next
              else:
                 tmp=ListNode(l2.val)
                 l2=l2.next
              a.next=tmp
              a=a.next
        a.next=l1 if l1 else l2
        return b.next
    
    #合并k个有序列表,将所有列表中的值先取出放进一个list中，sort排序再依次链接，n*logn
    if not lists: return None
        t=len(lists)
        res=[]
        for i in range(t):
            if lists[i]:
                tmp=lists[i]
                while tmp:
                  res.append(tmp.val)
                  tmp=tmp.next
        res.sort()
        a=headnode=ListNode(0)
        for j in range(len(res)):
            tmpnode=ListNode(res[j])
            a.next=tmpnode
            a=a.next
        return headnode.next

    #合并k个有序列表,用最小堆实现,O(n*logk),k为链表的个数
    import heapq
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        t=len(lists)
        res=[]
        for index,i in enumerate(lists):
            #index为对应的链表
            #堆中按val值得大小存放(val,index)
            if i:
                heapq.heappush(res,(i.val,index))
        tmp=headnode=ListNode(-1)
        while res:
              v,index=heapq.heappop(res)
              #指向值最小的节点
              tmp.next=lists[index]
              tmp=tmp.next
              #index对应的链表指向下一个节点
              lists[index]=lists[index].next
              if lists[index]:
                 heapq.heappush(res,(lists[index].val,index)) 
        return headnode.next

     #链表倒数第k个节点，双指针遍法
     def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        before,after=head,head
        for i in range(k):
            after=after.next
        while after:
            before,after=before.next,after.next
        return before
     #判断某个链表是否有环：快慢指针，快的指针肯定会追上慢的指针，套圈问题
     def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        low=head
        fast=head.next
        while fast and fast.next:
             if fast==low: return True
             low=low.next
             fast=fast.next.next
        return False
    
