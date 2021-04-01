
# @Title: 两两交换链表中的节点 (Swap Nodes in Pairs)
# @Author: cocofe
# @Date: 2020-10-29 19:28:39
# @Runtime: 16 ms
# @Memory: 12.9 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre_head = ListNode(None)
        pre_head.next = head
        curr, nex = head, head.next
        prev = pre_head
        while nex:
            n_nex = nex.next
            curr.next = n_nex
            nex.next = curr
            prev.next = nex
            prev = curr
            curr = n_nex
            nex = curr.next if curr else None
        return pre_head.next

