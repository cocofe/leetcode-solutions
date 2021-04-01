
-- @Title: 查找重复的电子邮箱 (Duplicate Emails)
-- @Author: cocofe
-- @Date: 2020-10-27 00:02:54
-- @Runtime: 263 ms
-- @Memory: 0 B

# Write your MySQL query statement below

select Email from Person group by Email having count(*) > 1
