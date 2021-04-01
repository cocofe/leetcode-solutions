
| English | [简体中文](README.md) |

# [392. Is Subsequence](https://leetcode-cn.com/problems/is-subsequence/)

## Description

<p>Given two strings <code>s</code> and <code>t</code>, check if <code>s</code> is a <strong>subsequence</strong> of <code>t</code>.</p>

<p>A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;abcde&quot;</code> while <code>&quot;aec&quot;</code> is not).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abc", t = "ahbgdc"
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "axc", t = "ahbgdc"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 100</code></li>
	<li><code>0 &lt;= t.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code>&nbsp;consist&nbsp;only of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If there are lots of incoming <code>s</code>, say <code>s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub></code> where <code>k &gt;= 10<sup>9</sup></code>, and you want to check one by one to see if <code>t</code> has its subsequence. In this scenario, how would you change your code?

## Related Topics

- [Greedy](https://leetcode-cn.com/tag/greedy)
- [Binary Search](https://leetcode-cn.com/tag/binary-search)
- [Dynamic Programming](https://leetcode-cn.com/tag/dynamic-programming)

## Similar Questions

- [Number of Matching Subsequences](../number-of-matching-subsequences/README_EN.md)
- [Shortest Way to Form String](../shortest-way-to-form-string/README_EN.md)
