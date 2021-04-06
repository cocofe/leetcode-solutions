
# @Title: 排序链表 (Sort List)
# @Author: cocofe
# @Date: 2021-04-05 08:59:01
# @Runtime: 820 ms
# @Memory: 29.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        mid = self.sortList(mid)
        slow = self.sortList(head)
        h = ListNode(0)
        p = h
        while mid and slow:
            if slow.val <= mid.val:
                p.next = ListNode(slow.val)
                slow = slow.next
            else:
                p.next = ListNode(mid.val)
                mid = mid.next
            p = p.next
        while mid:
            p.next = ListNode(mid.val)
            mid = mid.next
            p = p.next
        while slow:
            p.next = ListNode(slow.val)
            slow = slow.next
            p = p.next
        return h.next


