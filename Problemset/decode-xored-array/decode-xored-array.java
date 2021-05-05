
// @Title: 解码异或后的数组 (Decode XORed Array)
// @Author: cocofe
// @Date: 2021-05-06 00:59:44
// @Runtime: 1 ms
// @Memory: 39.1 MB

class Solution {
    public int[] decode(int[] encoded, int first) {
        // a ^ b = c
        // b = b ^ a ^ a = c ^ a
        int[] ans = new int[encoded.length+1];
        ans[0] = first;
        for(int idx=0;idx < encoded.length;idx++){
            ans[idx+1] = ans[idx] ^ encoded[idx];
        }
        return ans;

    }
}
