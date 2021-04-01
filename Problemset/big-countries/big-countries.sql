
-- @Title: 大的国家 (Big Countries)
-- @Author: cocofe
-- @Date: 2020-10-27 00:23:47
-- @Runtime: 195 ms
-- @Memory: 0 B

# Write your MySQL query statement below

select name, population, area from world where area > 3000000 or population > 25000000
