
// @Title: 阶乘后的零 (Factorial Trailing Zeroes)
// @Author: cocofe
// @Date: 2021-05-03 01:50:05
// @Runtime: 6 ms
// @Memory: 35.4 MB

class Solution {
    public int trailingZeroes(int n) {
        /*
        可以理解为尾部的0是乘以10得到的, 所以 只要找到2和5的对数, 即可知道0的个数
        因为5的个数肯定比2小, 所以只需要5的个数即为结果
        */
        int c5 = 0;
        for(int i = 5; i <= n ; i += 5){
            int i5 = i;
            // System.out.println(c2);
            while(i5 > 0 && i5 % 5 == 0){
                c5 += 1;
                i5 /= 5;
            }
        }
        return c5;
    }
}
