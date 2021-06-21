
# @Title: 移除链表元素 (Remove Linked List Elements)
# @Author: cocofe
# @Date: 2021-06-19 11:05:01
# @Runtime: 84 ms
# @Memory: 17.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next
