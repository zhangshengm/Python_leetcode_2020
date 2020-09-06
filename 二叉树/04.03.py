# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #考虑层序遍历所有节点
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        root=[tree]
        if not tree: return []
        res=[ListNode(tree.val)]
        while root:
            t=[]
            for node in root:
                if node.left:
                   t.append(node.left)
                if node.right:
                   t.append(node.right)
            #临时节点指向每一层的第一个节点
            tmp=tmp1=ListNode(None)
            for node1 in t:
                tmp1.next=ListNode(node1.val)
                tmp1=tmp1.next
            #如果临时节点不为空则加入到结果列表中
            if tmp.next:
               res.append(tmp.next)
            root=t
        # print(res)
        return res
