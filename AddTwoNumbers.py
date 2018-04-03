# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    
    Example
    
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = num2 = 0
        idx_1 = idx_2 = 0
        while l1 is not None:
            num1 += 10 ** idx_1 * l1.val
            l1 = l1.next
            idx_1 += 1
        while l2 is not None:
            num2 += 10 ** idx_2 * l2.val
            l2 = l2.next
            idx_2 += 1
        total = num1 + num2
        root = ListNode(total % 10)
        total = total // 10
        current = root
        while total != 0:
            tmp_node = ListNode(total % 10)
            total = total // 10
            current.next = tmp_node
            current = tmp_node
        return root

    def test(self):
        l1 = [2,4,3]
        l2 = [5,6,4]
        current = None
        root1 = root2 = None
        for idx, val in enumerate(l1):
            if idx == 0:
                root1 = ListNode(val)
                current = root1
            else:
                tmp = ListNode(val)
                current.next = tmp
                current = tmp

        for idx, val in enumerate(l2):
            if idx == 0:
                root2 = ListNode(val)
                current = root2
            else:
                tmp = ListNode(val)
                current.next = tmp
                current = tmp
        self.addTwoNumbers(root1, root2)


