
// @Title: 斐波那契数 (Fibonacci Number)
// @Author: cocofe
// @Date: 2021-07-17 01:08:41
// @Runtime: 0 ms
// @Memory: 35.3 MB

class Solution {
    public int fib(int n) {
        int a = 0, b = 1;
        if (n <= 1) {
            return n;
        } else {
            for (int j = 2; j <= n; j ++) {
                int tmp = a;
                a = b;
                b += tmp;
            }
            return b;
        }
    }
}
