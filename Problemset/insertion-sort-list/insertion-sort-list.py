
# @Title: 对链表进行插入排序 (Insertion Sort List)
# @Author: cocofe
# @Date: 2021-04-28 02:01:23
# @Runtime: 1180 ms
# @Memory: 16.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        root = ListNode(None)
        s, e = head, head
        root.next = s
        curr = e.next
        e.next = None
        while curr:
            p = root.next
            prev = root
            next_curr = curr.next
            while p and p.val < curr.val:
                prev = p
                p = p.next
            prev.next, curr.next = curr, prev.next 
            curr = next_curr
        return root.next
