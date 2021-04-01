
# @Title: 下一个排列 (Next Permutation)
# @Author: cocofe
# @Date: 2021-03-13 01:49:02
# @Runtime: 16 ms
# @Memory: 13 MB

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        curr, nex = len(nums) - 2, len(nums) - 1
        while curr >= 0:
            if nums[curr] >= nums[nex]:
                curr -= 1
                nex -= 1
            else:
                # 当前元素比下一个元素小
                # 要尽可能将curr 与 [nex:] 中尽可能靠右的元素进行交换
                # 365431 -> 3 和 4 交换
                for k in range(len(nums)-1, curr, -1):
                    if nums[k] > nums[curr]:
                        # print 'switch {} to {}'.format(curr, k)
                        nums[k], nums[curr] = nums[curr], nums[k]
                        # print 'after switch ', nums
                        nums[curr+1:] = sorted(nums[curr+1:])
                        return
        nums.sort()

