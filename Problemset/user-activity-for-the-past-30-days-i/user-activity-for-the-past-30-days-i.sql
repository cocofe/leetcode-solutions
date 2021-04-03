
-- @Title: 查询近30天活跃用户数 (User Activity for the Past 30 Days I)
-- @Author: cocofe
-- @Date: 2021-04-03 12:44:21
-- @Runtime: 294 ms
-- @Memory: 0 B

# Write your MySQL query statement below
select activity_date as day, count(distinct user_id) as active_users from Activity
where activity_date between '2019-06-28' and '2019-07-27'
group by activity_date 
