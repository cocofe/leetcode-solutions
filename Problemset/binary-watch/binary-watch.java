
// @Title: 二进制手表 (Binary Watch)
// @Author: cocofe
// @Date: 2021-06-22 00:31:22
// @Runtime: 12 ms
// @Memory: 38.5 MB

class Solution {
    public List<String> readBinaryWatch(int turnedOn) {
        List<String> ans = new LinkedList<>();
        for(int i=0; i < 1024 ; i++){
            int h = i >> 6, m = i & 0b0000111111;
            if (h <= 11 && m <= 59 && (Integer.bitCount(i)==turnedOn)){
                ans.add(""+h+":"+ (m > 9? m: "0" + m));
            }
        }
        return ans;
    }
}
