
-- @Title: 变更性别 (Swap Salary)
-- @Author: cocofe
-- @Date: 2020-10-27 00:18:47
-- @Runtime: 212 ms
-- @Memory: 0 B

# Write your MySQL query statement below
update salary set sex = case sex when 'm' then 'f' else 'm' end
