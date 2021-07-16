
// @Title: 第 N 个泰波那契数 (N-th Tribonacci Number)
// @Author: cocofe
// @Date: 2021-07-17 01:15:18
// @Runtime: 0 ms
// @Memory: 35.3 MB

class Solution {
    public int tribonacci(int n) {
        int a = 0, b = 1, c = 1;
        if (n <= 1) {
            return n; 
        } else if (n == 2) {
            return 1;
        } else {
            for (int i = 3; i<=n; i++) {
                int tmp = a;
                int tmp2 = b;
                a = b;
                b = c;
                c += tmp + tmp2;
            }
            return c;
        }
    }
}
