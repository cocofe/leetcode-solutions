
// @Title: 把数字翻译成字符串 (把数字翻译成字符串 LCOF)
// @Author: cocofe
// @Date: 2021-07-18 03:15:58
// @Runtime: 0 ms
// @Memory: 35.2 MB

class Solution {

    public int translateNum(int num) {
        String str = String.valueOf(num);
        int[] dp = new int[str.length()];
        dp[0] = 1;
        for (int i = 1; i < str.length(); i++) {
            dp[i] = dp[i-1];
            if (i - 1 >= 0 && 
            Integer.valueOf(str.substring(i-1, i+1)) >= 10 && 
            Integer.valueOf(str.substring(i-1, i+1)) <= 25
            ) {
                dp[i] += i - 2 >= 0 ? dp[i-2] : 1;
            }
        }
        return dp[str.length()-1];

    }
}
