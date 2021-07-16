
// @Title: 根据字符出现频率排序 (Sort Characters By Frequency)
// @Author: cocofe
// @Date: 2021-07-06 00:02:43
// @Runtime: 19 ms
// @Memory: 39.4 MB

class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i=0; i < s.length(); i++){
            char ch = s.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        List<Character> list = new ArrayList<Character>(map.keySet());
        Collections.sort(list, (a, b) -> (map.get(b) - map.get(a)));
        StringBuilder sb = new StringBuilder();
        for (char ch: list) {
            for(int i = 0; i<map.get(ch);i++){
                sb.append(ch);
            }
        }
        return sb.toString();
    }
}
