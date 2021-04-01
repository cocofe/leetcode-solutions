
# @Title: 有序链表转换二叉搜索树 (Convert Sorted List to Binary Search Tree)
# @Author: cocofe
# @Date: 2020-10-29 20:01:11
# @Runtime: 116 ms
# @Memory: 25 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return
        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.next
        def helper(start, end):
            mid = (start+end) / 2
            root = ListNode(nums[mid])
            root.left = helper(start, mid-1) if start <= mid - 1 else None
            root.right = helper(mid + 1, end) if mid + 1 <= end else None
            return root
        return helper(0, len(nums)-1)

