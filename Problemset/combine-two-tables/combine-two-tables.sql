
-- @Title: 组合两个表 (Combine Two Tables)
-- @Author: cocofe
-- @Date: 2021-03-09 00:33:04
-- @Runtime: 258 ms
-- @Memory: 0 B

# Write your MySQL query statement below
select Person.FirstName, Person.LastName, Address.City, Address.State from Person left join Address on Person.PersonId = Address.PersonId;
