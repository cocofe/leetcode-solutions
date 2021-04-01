
# @Title: 链表的中间结点 (Middle of the Linked List)
# @Author: cocofe
# @Date: 2020-10-30 22:02:07
# @Runtime: 24 ms
# @Memory: 12.9 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            if not fast.next:
                break
            fast = fast.next.next
        return slow
        
