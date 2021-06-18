
// @Title: 串联字符串的最大长度 (Maximum Length of a Concatenated String with Unique Characters)
// @Author: cocofe
// @Date: 2021-06-19 02:55:36
// @Runtime: 3 ms
// @Memory: 35.9 MB

class Solution {
    int ans = 0;
    public int maxLength(List<String> arr) {
        LinkedList<Integer> masks = new LinkedList();
        for(String s:arr) {
            int mask = 0;
            for(int i=0; i<s.length();i++){
                int offset = s.charAt(i) - 'a';
                if (((mask >> offset) & 1) == 1){
                    mask=0;
                    break;
                }
                mask |= 1 << offset;
            }
            if (mask > 0){
                masks.add(mask);
            }
        }
        // System.out.println(masks);
        backtrace(0, 0, masks);
        return ans;
    }
    public void backtrace(int idx, int mask, LinkedList<Integer> masks) {
        if(idx == masks.size()){
            ans = Math.max(ans, Integer.bitCount(mask));
            return;
        }
        // System.out.println("" + (mask ^ masks.get(idx)) + "|" + mask + "|" + masks.get(idx));

        if((mask & masks.get(idx)) == 0) {
            backtrace(idx+1, mask | masks.get(idx), masks);
        }
        backtrace(idx+1, mask, masks);

    }
}
