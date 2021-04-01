
# @Title: 四数之和 (4Sum)
# @Author: cocofe
# @Date: 2021-02-18 13:23:34
# @Runtime: 2892 ms
# @Memory: 13.2 MB

class Solution(object):
    def two_sum(self, nums, target):
        mapping = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            mapping[num].append(idx)
        ans = []
        prev = None
        for idx in range(len(nums)-1):
            if nums[idx] == prev:
                continue
            idxs = mapping[target - nums[idx]]
            prev = nums[idx]
            p = None
            for i in idxs:
                if i <= idx:
                    continue
                if nums[i] == p:
                    continue
                p = nums[i]
                ans.append([nums[idx], nums[i]])
        return ans
    
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        prev = None
        ans = []
        for idx in range(len(nums)-2):
            if nums[idx] == prev:
                continue
            ret = self.two_sum(nums[idx+1:], target - nums[idx])
            for avaliable_ans in ret:
                ans.append([nums[idx]] + avaliable_ans)
            prev = nums[idx]
        return ans

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        prev = None
        ans = []
        for idx in range(len(nums)-3):
            if nums[idx] == prev:
                continue
            prev = nums[idx]
            ret = self.threeSum(nums[idx+1:], target-nums[idx])
            for avaliable_ans in ret:
                ans.append([nums[idx]] + avaliable_ans)
        return ans
        
