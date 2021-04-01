
# @Title: 特定深度节点链表 (List of Depth LCCI)
# @Author: cocofe
# @Date: 2020-12-21 21:37:33
# @Runtime: 24 ms
# @Memory: 12.9 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def listOfDepth(self, tree):
        """
        :type tree: TreeNode
        :rtype: List[ListNode]
        """
        q = collections.deque()
        ans = []
        if not tree: return ans
        ans.append(ListNode(tree.val))
        q.append(tree)
        while q:
            head = ListNode(None)
            cur = head
            for _ in range(len(q)):
                node = q.popleft()
                for _node in (node.left, node.right):
                    if not _node:
                        continue
                    q.append(_node)
                    cur.next = ListNode(_node.val)
                    cur = cur.next
            if head.next:
                ans.append(head.next)
        return ans
                

