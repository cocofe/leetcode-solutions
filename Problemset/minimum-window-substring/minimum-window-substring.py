
# @Title: 最小覆盖子串 (Minimum Window Substring)
# @Author: cocofe
# @Date: 2020-10-16 21:50:39
# @Runtime: 632 ms
# @Memory: 14.7 MB

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left, right = 0, 0
        need = collections.Counter(t)
        windows = []
        def is_enough():
            return all([_v <= 0 for _v in need.values()])

        ans = None
        while right < len(s):
            to_add = s[right]
            if to_add in need:
                need[to_add] -= 1
            windows.append(to_add)
            if is_enough():
                while left <= right:
                    to_pop = windows[left]
                    if to_pop in need and need[to_pop] < 0:
                        left += 1
                        need[to_pop] += 1
                        continue
                    if to_pop not in need:
                        left += 1
                        continue
                    is_end = False
                    _ans = ''.join(windows[left:right+1])
                    ans = _ans if ans is None or len(ans) > len(_ans) else ans
                    # print _ans, windows, left, right, need
                    if to_pop in need:
                        need[to_pop] += 1
                        if need[to_pop] > 0:
                            is_end = True
                            # pop left unuse char
                            left += 1
                            while left <= right:  
                                to_pop = windows[left]
                                if to_pop in need and need[to_pop] > -1:
                                    break
                                if to_pop in need:
                                    need[to_pop] += 1
                                left += 1
                    else:     
                        left += 1
                    if is_end:
                        break
            right += 1
        return ans or ''
            
                    
        
