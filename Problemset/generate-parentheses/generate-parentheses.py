
# @Title: 括号生成 (Generate Parentheses)
# @Author: cocofe
# @Date: 2020-11-03 22:45:21
# @Runtime: 44 ms
# @Memory: 13.3 MB

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def track(path, choices):
            left = choices['(']
            right = choices[')']
            if left == 0 and right == 0:
                ans.append(''.join(path))
                return
            tmp = path[:]
            optional = []
            if left == right:
                # 选择左括号
                optional.append('(')
            else:
                optional = [')']
                if left > 0:
                    optional.append('(')
            # print 'choices {}, optional {}, path {}'.format(choices, optional, path)
            for choice in optional:
                path.append(choice)
                _choices = copy.copy(choices)
                _choices[choice] -= 1
                track(path, _choices)
                path = tmp
        track([], {'(': n, ')': n})
        return ans


