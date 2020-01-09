# -*- coding: UTF-8 -*-
from collections import defaultdict


class Solution(object):
    """
    Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

    Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.
    Example 1:

    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".
    Example 2:

    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
                 Note that you are allowed to reuse a dictionary word.
    Example 3:

    Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: false
    """

    def _wordBreak(self, s, wordDict, begin, end, dp):
        tmp = ''
        if begin >= end:
            return True
        if begin in dp and end in dp[begin]:
            return dp[begin][end]
        ret = []
        for i in range(begin, end):
            tmp += s[i]
            if tmp in wordDict:
                ret.append(self._wordBreak(s, wordDict, i + 1, end, dp))
        dp[begin][end] = any(ret)
        return dp[begin][end]

    def wordBreak(self, s, wordDict):
        """
        解题思路:
            动态规划解决步骤基本都可以通过树的形式来表达
            对于任意长度字符, 皆可以分成两部分,
            一部分是字符串的首个字母为起点的连续字符串, 这个字符串与wordDict中某个字符串相同,
            这一部分可以看做树的父节点

            另一部分则是剩余字符串生成的一棵树

            假设 i, j 为字符串的索引, dp[i][j] 表示range(i,j)位置的字符串是否可被分割, 值是True/False

            dp[i][j] = dp[i+n][j] (如果存在i为起点长度为n的字符串)
            dp[i][j] = False (不存在i为起点长度为n的字符串)


        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        ret = []
        tmp = ''
        dp = defaultdict(dict)
        for i in range(0, length):
            tmp += s[i]
            if tmp in wordDict:
                ret.append(self._wordBreak(s, wordDict, i + 1, length, dp))
        return any(ret)

    def test(self):
        test_case = [
            {
                's': 'fohhemkkaecojceoaejkkoedkofhmohkcjmkggcmnami',
                'wordDict': ["kfomka", "hecagbngambii", "anobmnikj", "c",
                             "nnkmfelneemfgcl", "ah", "bgomgohl", "lcbjbg",
                             "ebjfoiddndih", "hjknoamjbfhckb", "eioldlijmmla",
                             "nbekmcnakif", "fgahmihodolmhbi", "gnjfe", "hk",
                             "b", "jbfgm", "ecojceoaejkkoed", "cemodhmbcmgl",
                             "j", "gdcnjj", "kolaijoicbc", "liibjjcini",
                             "lmbenj", "eklingemgdjncaa", "m", "hkh", "fblb",
                             "fk", "nnfkfanaga", "eldjml", "iejn",
                             "gbmjfdooeeko", "jafogijka", "ngnfggojmhclkjd",
                             "bfagnfclg", "imkeobcdidiifbm", "ogeo", "gicjog",
                             "cjnibenelm", "ogoloc", "edciifkaff", "kbeeg",
                             "nebn", "jdd", "aeojhclmdn", "dilbhl", "dkk",
                             "bgmck", "ohgkefkadonafg", "labem", "fheoglj",
                             "gkcanacfjfhogjc", "eglkcddd", "lelelihakeh",
                             "hhjijfiodfi", "enehbibnhfjd", "gkm", "ggj", "ag",
                             "hhhjogk", "lllicdhihn", "goakjjnk", "lhbn",
                             "fhheedadamlnedh", "bin", "cl", "ggjljjjf",
                             "fdcdaobhlhgj", "nijlf", "i", "gaemagobjfc", "dg",
                             "g", "jhlelodgeekj", "hcimohlni", "fdoiohikhacgb",
                             "k", "doiaigclm", "bdfaoncbhfkdbjd", "f",
                             "jaikbciac", "cjgadmfoodmba", "molokllh",
                             "gfkngeebnggo", "lahd", "n", "ehfngoc", "lejfcee",
                             "kofhmoh", "cgda", "de", "kljnicikjeh",
                             "edomdbibhif", "jehdkgmmofihdi", "hifcjkloebel",
                             "gcghgbemjege", "kobhhefbbb", "aaikgaolhllhlm",
                             "akg", "kmmikgkhnn", "dnamfhaf", "mjhj",
                             "ifadcgmgjaa", "acnjehgkflgkd", "bjj", "maihjn",
                             "ojakklhl", "ign", "jhd", "kndkhbebgh",
                             "amljjfeahcdlfdg", "fnboolobch", "gcclgcoaojc",
                             "kfokbbkllmcd", "fec", "dljma", "noa", "cfjie",
                             "fohhemkka", "bfaldajf", "nbk", "kmbnjoalnhki",
                             "ccieabbnlhbjmj", "nmacelialookal",
                             "hdlefnbmgklo", "bfbblofk", "doohocnadd", "klmed",
                             "e", "hkkcmbljlojkghm", "jjiadlgf",
                             "ogadjhambjikce", "bglghjndlk", "gackokkbhj",
                             "oofohdogb", "leiolllnjj", "edekdnibja",
                             "gjhglilocif", "ccfnfjalchc", "gl", "ihee",
                             "cfgccdmecem", "mdmcdgjelhgk", "laboglchdhbk",
                             "ajmiim", "cebhalkngloae", "hgohednmkahdi",
                             "ddiecjnkmgbbei", "ajaengmcdlbk", "kgg",
                             "ndchkjdn", "heklaamafiomea", "ehg",
                             "imelcifnhkae", "hcgadilb", "elndjcodnhcc",
                             "nkjd", "gjnfkogkjeobo", "eolega", "lm",
                             "jddfkfbbbhia", "cddmfeckheeo", "bfnmaalmjdb",
                             "fbcg", "ko", "mojfj", "kk", "bbljjnnikdhg", "l",
                             "calbc", "mkekn", "ejlhdk", "hkebdiebecf",
                             "emhelbbda", "mlba", "ckjmih", "odfacclfl",
                             "lgfjjbgookmnoe", "begnkogf", "gakojeblk",
                             "bfflcmdko", "cfdclljcg", "ho", "fo", "acmi",
                             "oemknmffgcio", "mlkhk", "kfhkndmdojhidg",
                             "ckfcibmnikn", "dgoecamdliaeeoa", "ocealkbbec",
                             "kbmmihb", "ncikad", "hi", "nccjbnldneijc",
                             "hgiccigeehmdl", "dlfmjhmioa", "kmff", "gfhkd",
                             "okiamg", "ekdbamm", "fc", "neg", "cfmo",
                             "ccgahikbbl", "khhoc", "elbg", "cbghbacjbfm",
                             "jkagbmfgemjfg", "ijceidhhajmja", "imibemhdg",
                             "ja", "idkfd", "ndogdkjjkf", "fhic", "ooajkki",
                             "fdnjhh", "ba", "jdlnidngkfffbmi",
                             "jddjfnnjoidcnm", "kghljjikbacd", "idllbbn", "d",
                             "mgkajbnjedeiee", "fbllleanknmoomb", "lom",
                             "kofjmmjm", "mcdlbglonin", "gcnboanh", "fggii",
                             "fdkbmic", "bbiln", "cdjcjhonjgiagkb",
                             "kooenbeoongcle", "cecnlfbaanckdkj", "fejlmog",
                             "fanekdneoaammb", "maojbcegdamn", "bcmanmjdeabdo",
                             "amloj", "adgoej", "jh", "fhf", "cogdljlgek", "o",
                             "joeiajlioggj", "oncal", "lbgg", "elainnbffk",
                             "hbdi", "femcanllndoh", "ke", "hmib",
                             "nagfahhljh", "ibifdlfeechcbal", "knec",
                             "oegfcghlgalcnno", "abiefmjldmln", "mlfglgni",
                             "jkofhjeb", "ifjbneblfldjel", "nahhcimkjhjgb",
                             "cdgkbn", "nnklfbeecgedie", "gmllmjbodhgllc",
                             "hogollongjo", "fmoinacebll", "fkngbganmh",
                             "jgdblmhlmfij", "fkkdjknahamcfb", "aieakdokibj",
                             "hddlcdiailhd", "iajhmg", "jenocgo", "embdib",
                             "dghbmljjogka", "bahcggjgmlf", "fb", "jldkcfom",
                             "mfi", "kdkke", "odhbl", "jin", "kcjmkggcmnami",
                             "kofig", "bid", "ohnohi", "fcbojdgoaoa", "dj",
                             "ifkbmbod", "dhdedohlghk", "nmkeakohicfdjf",
                             "ahbifnnoaldgbj", "egldeibiinoac", "iehfhjjjmil",
                             "bmeimi", "ombngooicknel", "lfdkngobmik",
                             "ifjcjkfnmgjcnmi", "fmf", "aoeaa", "an",
                             "ffgddcjblehhggo", "hijfdcchdilcl",
                             "hacbaamkhblnkk", "najefebghcbkjfl",
                             "hcnnlogjfmmjcma", "njgcogemlnohl", "ihejh", "ej",
                             "ofn", "ggcklj", "omah", "hg", "obk", "giig",
                             "cklna", "lihaiollfnem", "ionlnlhjckf",
                             "cfdlijnmgjoebl", "dloehimen", "acggkacahfhkdne",
                             "iecd", "gn", "odgbnalk", "ahfhcd", "dghlag",
                             "bchfe", "dldblmnbifnmlo", "cffhbijal",
                             "dbddifnojfibha", "mhh", "cjjol", "fed", "bhcnf",
                             "ciiibbedklnnk", "ikniooicmm", "ejf",
                             "ammeennkcdgbjco", "jmhmd", "cek", "bjbhcmda",
                             "kfjmhbf", "chjmmnea", "ifccifn", "naedmco",
                             "iohchafbega", "kjejfhbco", "anlhhhhg"]
            },
            {'s': "acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb",
             'wordDict': [
                 "abbcbda", "cbdaaa", "b", "dadaaad", "dccbbbc", "dccadd",
                 "ccbdbc", "bbca", "bacbcdd", "a", "bacb", "cbc", "adc", "c",
                 "cbdbcad", "cdbab", "db", "abbcdbd", "bcb", "bbdab", "aa",
                 "bcadb", "bacbcb", "ca", "dbdabdb", "ccd", "acbb", "bdc",
                 "acbccd", "d", "cccdcda", "dcbd", "cbccacd", "ac", "cca",
                 "aaddc", "dccac", "ccdc", "bbbbcda", "ba", "adbcadb", "dca",
                 "abd", "bdbb", "ddadbad", "badb", "ab", "aaaaa", "acba",
                 "abbb"]}
        ]
        for case in test_case:
            print self.wordBreak(case['s'], case['wordDict'])
