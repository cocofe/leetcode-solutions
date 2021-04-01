
-- @Title: 第二高的薪水 (Second Highest Salary)
-- @Author: cocofe
-- @Date: 2020-12-24 20:42:26
-- @Runtime: 157 ms
-- @Memory: 0 B

# Write your MySQL query statement below
select (select distinct(Salary) as SecondHighestSalary from Employee order by Salary desc limit 1,1) as SecondHighestSalary
