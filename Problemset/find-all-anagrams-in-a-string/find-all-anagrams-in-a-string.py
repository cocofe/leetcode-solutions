
# @Title: 找到字符串中所有字母异位词 (Find All Anagrams in a String)
# @Author: cocofe
# @Date: 2020-10-16 22:59:27
# @Runtime: 248 ms
# @Memory: 14.1 MB

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 是字符串的一个排列, 只要保证字符的种类和数量一致就行
        s1, s2 = p, s
        if not s1: return True
        left, right = 0, 0
        need = collections.Counter(s1)
        ans = []
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
                        ans.append(left)
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
                
        return ans
