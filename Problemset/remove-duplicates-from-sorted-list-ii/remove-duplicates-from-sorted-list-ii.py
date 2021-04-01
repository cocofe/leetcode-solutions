
# @Title: 删除排序链表中的重复元素 II (Remove Duplicates from Sorted List II)
# @Author: cocofe
# @Date: 2021-03-25 09:24:53
# @Runtime: 20 ms
# @Memory: 13 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_head = ListNode(None)
        prev_head.next = head
        prev = prev_head
        curr = head
        while curr:
            nex = curr.next
            is_dup = False
            while nex and nex.val == curr.val:
                is_dup = True
                curr = nex
                nex = nex.next

            if not is_dup:
               prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
        return prev_head.next
