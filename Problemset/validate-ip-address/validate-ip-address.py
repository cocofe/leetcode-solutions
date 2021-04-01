
# @Title: 验证IP地址 (Validate IP Address)
# @Author: cocofe
# @Date: 2020-03-05 01:37:35
# @Runtime: 8 ms
# @Memory: N/A

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        strings = IP.split('.')
        length = len(strings)
        is_v4 = True
        if length != 4:
            is_v4 = False
        else:
            for s in strings:
                if not s.isdigit():
                    is_v4 = False
                    break
                int_s = int(s)
                if str(int_s) != s:
                    is_v4 = False
                    break
                if int_s < 0 or int_s > 255:
                    is_v4 = False
                    break
        if is_v4:
            return 'IPv4'
        is_v6 = True
        strings = IP.split(':')
        ava_char = ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if len(strings) != 8:
            is_v6 = False
        else:
            for s in strings:
                length = len(s)
                if length == 0 or length > 4:
                    is_v6 = False
                    break
                else:
                    for _s in s:
                        if _s not in ava_char:
                            is_v6 = False
                            break
        if is_v6:
            return 'IPv6'
        return 'Neither'
            
            
                
        
        
