
-- @Title: 寻找用户推荐人 (Find Customer Referee)
-- @Author: cocofe
-- @Date: 2021-04-03 14:10:07
-- @Runtime: 341 ms
-- @Memory: 0 B

# Write your MySQL query statement below

select name from customer where referee_id is null or referee_id != 2
