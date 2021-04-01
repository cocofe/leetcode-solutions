
# @Title: 链表中倒数第k个节点 (链表中倒数第k个节点 LCOF)
# @Author: cocofe
# @Date: 2020-08-17 00:53:24
# @Runtime: 24 ms
# @Memory: 12.3 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p1 = head
        idx = 1
        while idx < k:
            idx += 1
            p1 = p1.next
        p = head
        ans = None
        while p and p1:
            ans = p
            p = p.next
            p1 = p1.next
        return ans
        
