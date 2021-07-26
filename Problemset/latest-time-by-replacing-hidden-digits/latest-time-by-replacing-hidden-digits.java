
// @Title: 替换隐藏数字得到的最晚时间 (Latest Time by Replacing Hidden Digits)
// @Author: cocofe
// @Date: 2021-07-24 12:01:23
// @Runtime: 0 ms
// @Memory: 36.6 MB

class Solution {
    public String maximumTime(String time) {
        char h1 = time.charAt(0);
        char h2 = time.charAt(1);
        char m1 = time.charAt(3);
        char m2 = time.charAt(4);
        if (h1 == '?' && h2 == '?') {
            h1 = '2';
            h2 = '3';
        } else if ( h1 == '?') {
            if (h2 > '3') {
                h1 = '1';
            } else {
                h1 = '2';
            }
        } else if ( h2 == '?') {
            if (h1 == '2') {
                h2 = '3';
            } else {
                h2 = '9';
            }
        }
        if ( m1 == '?') {
            m1 = '5';
        }
        if ( m2 == '?') {
            m2 = '9';
        }
        StringBuilder sb = new StringBuilder();
        sb.append(h1);
        sb.append(h2);
        sb.append(':');
        sb.append(m1);
        sb.append(m2);
        return sb.toString();

    }
}
