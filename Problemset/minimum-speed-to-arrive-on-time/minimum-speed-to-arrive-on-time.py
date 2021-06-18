
# @Title: 准时到达的列车最小时速 (Minimum Speed to Arrive on Time)
# @Author: cocofe
# @Date: 2021-05-23 11:24:50
# @Runtime: 6460 ms
# @Memory: 25.2 MB

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def is_arrive(speed):
            time_at = 0
            time_used = 0
            for d in dist:
                if time_at % 1 != 0:
                    time_used += (1 - time_at % 1)
                time_at = d / speed
                time_used += time_at
            # print(speed, time_used)
            return time_used <= hour
        _m = 10**9
        # print(_m)
        left, right = 1, _m
        while left <= right:
            mid = math.ceil(left + (right - left) // 2)
            if is_arrive(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if is_arrive(left) else -1
            
            
