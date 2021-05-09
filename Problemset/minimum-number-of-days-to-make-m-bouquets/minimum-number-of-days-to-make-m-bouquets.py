
# @Title: 制作 m 束花所需的最少天数 (Minimum Number of Days to Make m Bouquets)
# @Author: cocofe
# @Date: 2021-05-10 02:44:07
# @Runtime: 1968 ms
# @Memory: 25.2 MB

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(day):
            nums = [0 if d > day else 1 for d in bloomDay]
            cnt = 0
            p = 0
            flower_cnt = 0
            while p < len(nums) and cnt < m:
                if flower_cnt == k:
                    cnt += 1
                    flower_cnt = 0
                if nums[p] == 0:
                    flower_cnt = 0
                else:
                    flower_cnt += 1
                p += 1
            if flower_cnt == k:
                cnt += 1
            return cnt >= m
        if m * k > len(bloomDay):
            return -1
        left, right = min(bloomDay), max(bloomDay)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return -1 if left > max(bloomDay) else left

