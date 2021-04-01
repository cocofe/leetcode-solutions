
# @Title: 重排链表 (Reorder List)
# @Author: cocofe
# @Date: 2020-10-20 21:49:52
# @Runtime: 76 ms
# @Memory: 30.2 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next
        i, j = 0, len(nodes) - 1
        while i < j:
            # 将j插入到i之后
            nex = nodes[i].next
            nodes[i].next = nodes[j]
            nodes[j].next = nex
            i += 1
            j -= 1
        if i < len(nodes):
            nodes[i].next = None
