
| English | [简体中文](README.md) |

# [974. Subarray Sums Divisible by K](https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/)

## Description

<p>Given an array <code>nums</code> of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by <code>k</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-1-1">[4,5,0,-2,-3,1]</span>, k = <span id="example-input-1-2">5</span>
<strong>Output: </strong><span id="example-output-1">7</span>
<strong>Explanation: </strong>There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= nums.length &lt;= 30000</code></li>
	<li><code>-10000 &lt;= nums[i] &lt;= 10000</code></li>
	<li><code>2 &lt;= k &lt;= 10000</code></li>
</ol>
</div>


## Related Topics

- [Array](https://leetcode-cn.com/tag/array)
- [Hash Table](https://leetcode-cn.com/tag/hash-table)

## Similar Questions

- [Subarray Sum Equals K](../subarray-sum-equals-k/README_EN.md)
