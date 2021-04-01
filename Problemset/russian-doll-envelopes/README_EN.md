
| English | [简体中文](README.md) |

# [354. Russian Doll Envelopes](https://leetcode-cn.com/problems/russian-doll-envelopes/)

## Description

<p>You are given a 2D array of integers <code>envelopes</code> where <code>envelopes[i] = [w<sub>i</sub>, h<sub>i</sub>]</code> represents the width and the height of an envelope.</p>

<p>One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope&#39;s width and height.</p>

<p>Return <em>the maximum number of envelopes you can Russian doll (i.e., put one inside the other)</em>.</p>

<p><strong>Note:</strong> You cannot rotate an envelope.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> envelopes = [[5,4],[6,4],[6,7],[2,3]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The maximum number of envelopes you can Russian doll is <code>3</code> ([2,3] =&gt; [5,4] =&gt; [6,7]).
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> envelopes = [[1,1],[1,1],[1,1]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= envelopes.length &lt;= 5000</code></li>
	<li><code>envelopes[i].length == 2</code></li>
	<li><code>1 &lt;= w<sub>i</sub>, h<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>


## Related Topics

- [Binary Search](https://leetcode-cn.com/tag/binary-search)
- [Dynamic Programming](https://leetcode-cn.com/tag/dynamic-programming)

## Similar Questions

- [Longest Increasing Subsequence](../longest-increasing-subsequence/README_EN.md)
