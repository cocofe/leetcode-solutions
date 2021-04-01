
# @Title: IP 地址无效化 (Defanging an IP Address)
# @Author: cocofe
# @Date: 2020-01-26 17:21:21
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.', '[.]')
