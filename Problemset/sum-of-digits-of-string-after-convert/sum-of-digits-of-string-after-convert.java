
// @Title: 字符串转化后的各位数字之和 (Sum of Digits of String After Convert)
// @Author: cocofe
// @Date: 2021-07-25 10:57:08
// @Runtime: 3 ms
// @Memory: 38.3 MB

class Solution {
    public int getLucky(String s, int k) {
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            sb.append(ch - 'a'+1);
        }
        int sum = 0;
        while (k > 0) {
            sum = 0;
            for(int i=0; i<sb.length(); i++) {
                char ch = sb.charAt(i);
                sum += Integer.valueOf(String.valueOf(ch));
            }
            sb = new StringBuilder(String.valueOf(sum));
            k --;
        }
        return sum;


    }
}
