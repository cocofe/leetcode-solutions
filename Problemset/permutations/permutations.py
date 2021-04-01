
# @Title: 全排列 (Permutations)
# @Author: cocofe
# @Date: 2021-03-31 01:27:28
# @Runtime: 12 ms
# @Memory: 13.2 MB

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def backtrack(idx, path):
            if idx == len(nums):
                ans.append(path)
                return
            for i in range(idx, len(nums)):
                # 选取idx元素
                # 如果想选取idx之后的元素, 则将idx与idx之后的元素进行交换, 保证idx之后的元素是未访问的
                nums[i], nums[idx] = nums[idx], nums[i]
                path.append(nums[idx])
                backtrack(idx+1, path[:])
                path.pop()
                nums[i], nums[idx] = nums[idx], nums[i]
        backtrack(0, [])
        return ans

