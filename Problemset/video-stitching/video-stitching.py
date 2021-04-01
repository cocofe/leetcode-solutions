
# @Title: 视频拼接 (Video Stitching)
# @Author: cocofe
# @Date: 2020-10-24 23:38:41
# @Runtime: 20 ms
# @Memory: 13.2 MB

class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        clips = sorted(clips, key=lambda x: (x[0], x[1]))
        dp = collections.OrderedDict()
        tail = 0
        for start, end in clips:
            if start == 0:
                dp[end] = 1
                tail = max(tail, end)
                continue
            if start > tail or end in dp or end <= tail:
                continue
            ava = []
            for _end, count in dp.items():
                if _end >= start:
                    ava.append(count)
            dp[end] = min(ava or [0]) + 1
            tail = end
        for _end, count in dp.items():
            if _end >= T:
                return count
        return -1
                

