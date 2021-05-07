
// @Title: 数组异或操作 (XOR Operation in an Array)
// @Author: cocofe
// @Date: 2021-05-07 00:05:41
// @Runtime: 0 ms
// @Memory: 35.2 MB

class Solution {
    public int xorOperation(int n, int start) {
        int ans = 0;
        int num;
        for(int i = 0; i < n; i++){
            num = start + 2 * i;
            ans ^= num;
        }
        return ans;
    }
}
