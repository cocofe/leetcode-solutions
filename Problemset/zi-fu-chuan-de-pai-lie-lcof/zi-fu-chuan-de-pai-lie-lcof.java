
// @Title: 字符串的排列 (字符串的排列  LCOF)
// @Author: cocofe
// @Date: 2021-06-22 02:05:10
// @Runtime: 17 ms
// @Memory: 43.3 MB

class Solution {
    List<String> ans = new LinkedList<>();
    public String[] permutation(String s) {
    char[] chs = s.toCharArray();
    Arrays.sort(chs);
    backtrace(0, chs, new StringBuilder());
    String[] arrs = new String[ans.size()];
    return ans.toArray(arrs);
    }

    public void swap(char[] chs, int pos1, int pos2){
        if (pos1 == pos2) {
            return;
        }
        char tmp = chs[pos1];
        chs[pos1] = chs[pos2];
        chs[pos2] = tmp;
    }

    public void backtrace(int pos, char[] chs, StringBuilder chars){
        if(pos >= chs.length){
            ans.add(chars.toString());
            return;
        }
        HashSet fixed = new HashSet();
        for (int i=pos; i<chs.length; i++) {
            char ch = chs[i];
            if(fixed.contains(ch)){
                continue;
            }
            fixed.add(ch);
            chars.append(ch);
            swap(chs, pos, i);
            backtrace(pos+1, chs, chars);
            swap(chs, pos, i);
            chars.deleteCharAt(chars.length() - 1);
        }
    }
    
}
