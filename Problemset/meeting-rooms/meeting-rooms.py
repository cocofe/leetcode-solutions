
# @Title: 会议室 (Meeting Rooms)
# @Author: cocofe
# @Date: 2021-03-27 02:06:40
# @Runtime: 32 ms
# @Memory: 15.7 MB

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda interval: (interval[1], intervals[0]))
        start = intervals[0]
        idx = 1
        while idx < len(intervals):
            if intervals[idx][0] < start[1]:
                return False
            start = intervals[idx]
            idx += 1
        return True
