
// @Title: 整数反转 (Reverse Integer)
// @Author: cocofe
// @Date: 2021-05-03 00:58:28
// @Runtime: 1 ms
// @Memory: 35.6 MB

class Solution {
    public int reverse(int x) {
        int ret = 0;
        while (x != 0) {
            if (ret > Integer.MAX_VALUE / 10 || ret < Integer.MIN_VALUE / 10)
                return 0;
            ret = ret * 10 + x % 10;
            x /= 10;
        }
        return ret;
    }
}
