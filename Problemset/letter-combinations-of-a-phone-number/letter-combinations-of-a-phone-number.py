
# @Title: 电话号码的字母组合 (Letter Combinations of a Phone Number)
# @Author: cocofe
# @Date: 2020-11-09 22:59:02
# @Runtime: 16 ms
# @Memory: 13 MB

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        def backtrack(path, digit_idx):
            if digit_idx == len(digits):
                if path:
                    ans.append(''.join(path))
                return
            chars = mapping[digits[digit_idx]]
            for char in chars:
                tmp = path[:]
                path.append(char)
                backtrack(path, digit_idx + 1)
                path = tmp

        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        backtrack([], 0)
        return ans
        
