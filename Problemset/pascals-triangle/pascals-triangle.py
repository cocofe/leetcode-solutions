
# @Title: 杨辉三角 (Pascal's Triangle)
# @Author: cocofe
# @Date: 2020-08-16 17:13:21
# @Runtime: 16 ms
# @Memory: 12.5 MB

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for row in range(0, numRows):
            if not ans:
                ans.append([1])
                continue
            cols = [1]
            pre = ans[row - 1]
            for col in range(1, row+1):
                if col < len(pre):
                    num = pre[col] + pre[col - 1]
                else:
                    num = 1
                cols.append(num)
            ans.append(cols)
        return ans
