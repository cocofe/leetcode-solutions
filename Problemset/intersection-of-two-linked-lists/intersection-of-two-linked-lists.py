
# @Title: 相交链表 (Intersection of Two Linked Lists)
# @Author: cocofe
# @Date: 2020-04-01 00:43:11
# @Runtime: 200 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a, len_b = 0, 0
        p, q = headA, headB
        while p:
            len_a += 1
            p = p.next
        while q:
            len_b += 1
            q = q.next
        diff = abs(len_a - len_b)
        p, q = headA, headB
        while diff > 0:
            cursor = p if len_a > len_b else q
            diff -= 1
            cursor = cursor.next
            if len_a > len_b:
                p = cursor
            else:
                q = cursor
        while p and q:
            if p == q:
                return p
            p = p.next
            q = q.next
        return None
                
            
            
        
        
