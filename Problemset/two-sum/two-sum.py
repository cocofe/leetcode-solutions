
# @Title: 两数之和 (Two Sum)
# @Author: cocofe
# @Date: 2018-04-02 21:21:32
# @Runtime: 54 ms
# @Memory: N/A

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}  # 用来索引指定值对应的位置
        for idx, val in enumerate(nums):
            least = target - val
            if least in tmp:
                return [tmp[least], idx]
            else:
                tmp[val] = idx
        
