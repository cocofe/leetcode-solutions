
# @Title: 旋转链表 (Rotate List)
# @Author: cocofe
# @Date: 2021-03-27 01:33:33
# @Runtime: 24 ms
# @Memory: 13.2 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        k = k % length
        if k == 0:
            return head
        p, fast_p = head, head
        while k > 0:
            fast_p = fast_p.next
            k -= 1
        while fast_p.next:
            p = p.next
            fast_p = fast_p.next
        new_head = p.next
        p.next = None
        fast_p.next = head
        return new_head
        
        
        

        
        
