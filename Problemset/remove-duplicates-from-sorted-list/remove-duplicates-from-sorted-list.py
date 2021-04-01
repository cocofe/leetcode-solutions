
# @Title: 删除排序链表中的重复元素 (Remove Duplicates from Sorted List)
# @Author: cocofe
# @Date: 2021-03-26 00:07:53
# @Runtime: 24 ms
# @Memory: 13.1 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p, fast_p = head, head.next
        while fast_p:
            if fast_p.val != p.val:
                p = p.next
                p.val = fast_p.val
                fast_p = fast_p.next
            else:
                fast_p = fast_p.next
        p.next = None
        return head

