
-- @Title: 合作过至少三次的演员和导演 (Actors and Directors Who Cooperated At Least Three Times)
-- @Author: cocofe
-- @Date: 2021-04-03 14:13:16
-- @Runtime: 269 ms
-- @Memory: 0 B

# Write your MySQL query statement below

select actor_id , director_id from ActorDirector group by actor_id, director_id having count(timestamp) >= 3
