
# @Title: 子集 (Subsets)
# @Author: cocofe
# @Date: 2021-03-31 00:58:47
# @Runtime: 32 ms
# @Memory: 13.3 MB

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(path, idx, length):
            if len(path) == length:
                ans.append(path)
                return
            for i in range(idx, len(nums)):
                path.append(nums[i])
                dfs(path[:], i + 1, length)
                path.pop()
        for length in range(len(nums)+1):
            dfs([], 0, length)
        return ans
