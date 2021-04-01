
# @Title: 合并区间 (Merge Intervals)
# @Author: cocofe
# @Date: 2021-03-27 02:00:47
# @Runtime: 32 ms
# @Memory: 15.5 MB

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda ite: (ite[0], -ite[1]))
        start = 0
        idx = 1
        ans = [intervals[start]]
        while idx < len(intervals):
            st, et = intervals[idx]
            if st > ans[-1][1]:
                start = idx
                ans.append(intervals[idx])
            else:
                ans[-1][0] = min(ans[-1][0], st)
                ans[-1][1] = max(ans[-1][1], et)
            idx += 1
        return ans
            
            
