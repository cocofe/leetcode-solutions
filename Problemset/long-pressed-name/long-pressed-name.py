
# @Title: 长按键入 (Long Pressed Name)
# @Author: cocofe
# @Date: 2020-10-21 23:47:52
# @Runtime: 20 ms
# @Memory: 13 MB

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0
        prev_char = None
        while i < len(name) and j < len(typed):
            s1 = name[i]
            s2 = typed[j]
            if s1 == s2:
                i += 1
                j += 1
                prev_char = s1
            elif s2 == prev_char:
                j += 1
            else:
                return False
        while j < len(typed) and typed[j] == prev_char:
            j += 1
        return i == len(name) and j == len(typed)



