
# @Title: 字符串的排列 (Permutation in String)
# @Author: cocofe
# @Date: 2021-02-10 12:19:17
# @Runtime: 176 ms
# @Memory: 13.2 MB

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 是字符串的一个排列, 只要保证字符的种类和数量一致就行
        if not s1: return True
        left, right = 0, 0
        need = collections.Counter(s1)
        ans = None
        windows = []
        is_enough = lambda: all([_v <= 0 for _v in need.values()])
        while right < len(s2):
            to_add = s2[right]
            windows.append(to_add)
            if to_add in need:
                need[to_add] -= 1
            if is_enough():
                # shrink windows
                while left <= right:
                    to_pop = s2[left]
                    if to_pop in need and need[to_pop] < 0:
                        left += 1
                        need[to_pop] += 1
                        continue
                    if to_pop not in need:
                        left += 1
                        continue
                    if (right - left + 1) == len(s1):
                        return True
                    left += 1
                    need[to_pop] += 1
                    while left <= right:
                        to_pop = windows[left]
                        if to_pop not in need:
                            left += 1
                            continue
                        if need[to_pop] < 0:
                            need[to_pop] += 1
                            left += 1
                            continue
                        break
                    break
            right += 1
                
        return False
