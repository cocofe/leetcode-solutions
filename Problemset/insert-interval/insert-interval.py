
# @Title: 插入区间 (Insert Interval)
# @Author: cocofe
# @Date: 2020-11-05 22:53:03
# @Runtime: 24 ms
# @Memory: 14.6 MB

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals: return [newInterval]
        start, end = None, None
        s_tmp, e_tmp = None, None
        ns, ne = newInterval
        for idx, (s, e) in enumerate(intervals):
            if s <= ns <= e:
                start = idx
            if s <= ne <= e:
                end = idx 
            if start is not None and end is not None:
                break
            if start is None and s_tmp is None and ns < s:
                s_tmp = idx
            if end is None and ne > e:
                e_tmp = idx
        # print start, end, s_tmp, e_tmp
        if start is None:
            start = s_tmp
        if end is None:
            end = e_tmp
        if start is not None and end is not None:
            _s, _ = intervals[start]
            new_start = min(_s, ns)
            _, _e = intervals[end]
            new_end = max(ne, _e)
            return intervals[:start] + [[new_start, new_end]] + intervals[end+1:]
        elif start is not None:
            return [newInterval] + intervals
        elif end is not None:
            return intervals + [newInterval]


