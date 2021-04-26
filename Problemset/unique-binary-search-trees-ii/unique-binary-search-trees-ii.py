
# @Title: 不同的二叉搜索树 II (Unique Binary Search Trees II)
# @Author: cocofe
# @Date: 2021-04-27 00:02:50
# @Runtime: 68 ms
# @Memory: 16.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(start, end):
            # 返回所有可选树合集
            if start > end:
                return [None]
            trees = []
            # choice root node
            for i in range(start, end+1):
                left_trees = helper(start, i-1)
                right_trees = helper(i+1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees
        return helper(1, n)


