
# @Title: 全排列 II (Permutations II)
# @Author: cocofe
# @Date: 2021-03-31 02:08:09
# @Runtime: 32 ms
# @Memory: 13.3 MB

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums = sorted(nums)
        def backtrack(idx, path):
            if idx == len(nums):
                ans.append(path)
            choices = set()
            for i in range(idx, len(nums)):
                # 重点是去重逻辑
                # 保证选择的元素之前没选择过, 这边要注意, 如果只关心不与上传选择的元素重复的话, 会有重复元素出现, 因为数组经过swap, 所以是无序的, 不能这样去重
                if nums[i] in choices:
                    continue
                nums[i], nums[idx] = nums[idx], nums[i]
                path.append(nums[idx])
                choices.add(nums[idx])
                backtrack(idx+1, path[:])
                path.pop()
                nums[i], nums[idx] = nums[idx], nums[i]
        backtrack(0, [])
        return ans

