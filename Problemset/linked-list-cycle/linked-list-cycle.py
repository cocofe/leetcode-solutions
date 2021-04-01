
# @Title: 环形链表 (Linked List Cycle)
# @Author: cocofe
# @Date: 2020-04-01 12:56:18
# @Runtime: 44 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        p = head
        p_2 = head.next.next
        while p and p_2:
            if p == p_2:
                return True
            p = p.next
            p_2 = p_2.next
            if not p_2:
                return False
            p_2 = p_2.next
        return False
        
