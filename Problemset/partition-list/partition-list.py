
# @Title: 分隔链表 (Partition List)
# @Author: cocofe
# @Date: 2020-10-29 23:05:38
# @Runtime: 28 ms
# @Memory: 13.4 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        min_head = ListNode(None)
        max_head = ListNode(None)
        p = head
        min_p, max_p = min_head, max_head
        while p:
            nex = p.next
            if p.val < x:
                min_p.next = p
                min_p = min_p.next
                min_p.next = None
            else:
                max_p.next = p
                max_p = max_p.next
                max_p.next = None
            p = nex
        p = min_head
        while p and p.next:
            p = p.next
        p.next = max_head.next
        return min_head.next
        
            
