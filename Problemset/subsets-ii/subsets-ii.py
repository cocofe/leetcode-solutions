
# @Title: 子集 II (Subsets II)
# @Author: cocofe
# @Date: 2021-03-31 00:49:53
# @Runtime: 28 ms
# @Memory: 13.3 MB

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums = sorted(nums)
        def backtrace(path, idx, length):
            # print path, idx, length
            if len(path) == length:
                return ans.append(path)
            prev = None
            for i in range(idx, len(nums)):
                if prev == nums[i]:
                    continue
                prev = nums[i]
                path.append(nums[i])
                backtrace(path[:], i + 1, length)
                path.pop()
        for length in range(len(nums)+1):
            backtrace([], 0, length)
        return ans
            
