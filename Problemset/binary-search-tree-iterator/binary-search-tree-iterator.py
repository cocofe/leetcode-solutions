
# @Title: 二叉搜索树迭代器 (Binary Search Tree Iterator)
# @Author: cocofe
# @Date: 2021-03-28 23:55:15
# @Runtime: 164 ms
# @Memory: 21.3 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        self.queue = collections.deque()
        self.inOrder(root)
    
    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        self.queue.append(root.val)
        self.inOrder(root.right)

    def next(self):
        return self.queue.popleft()


    def hasNext(self):
        return len(self.queue) > 0




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
