
# @Title: 合并两个有序链表 (Merge Two Sorted Lists)
# @Author: cocofe
# @Date: 2020-01-08 01:15:04
# @Runtime: 28 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lp = l1
        rp = l2
        new_node = ListNode(None)
        cp = new_node
        if not lp and not rp:
            return lp
        while lp and rp:
            if lp.val <= rp.val:
                val = lp.val
                lp = lp.next
            else:
                val = rp.val
                rp = rp.next
            if new_node.val is None:
                new_node.val = val
            else:
                node = ListNode(val)
                cp.next = node
                cp = cp.next
        while lp:
            if new_node.val is None:
                new_node.val = lp.val
            else:
                cp.next = lp
                cp = cp.next
            lp = lp.next
            
        while rp:
            if new_node.val is None:
                new_node.val = rp.val
            else:
                cp.next = rp
                cp = cp.next
            rp = rp.next
            
        return new_node
            
            
            
