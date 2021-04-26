
# @Title: 在 D 天内送达包裹的能力 (Capacity To Ship Packages Within D Days)
# @Author: cocofe
# @Date: 2021-04-26 14:35:55
# @Runtime: 316 ms
# @Memory: 17.1 MB

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def assume_days(w):
            day = 0
            _sum = 0
            for weight in weights:
                if _sum + weight <= w:
                    _sum += weight
                else:
                    day += 1
                    _sum = weight
            return day + 1

        left, right = max(weights), sum(weights)
        while left <= right:
            mid = left + (right - left) // 2
            days = assume_days(mid)
            if days > D:
                left = mid + 1
            else:
                right = mid - 1
        return left
