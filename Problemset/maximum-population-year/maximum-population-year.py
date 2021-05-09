
# @Title: 人口最多的年份 (Maximum Population Year)
# @Author: cocofe
# @Date: 2021-05-09 12:40:12
# @Runtime: 48 ms
# @Memory: 14.9 MB

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        nums = [0] * (2050 - 1950 + 1)
        for b, d in logs:
            for year in range(b, d):
                nums[year-1950] += 1
        max_cnt = max(nums)
        return nums.index(max_cnt) + 1950
            
        
