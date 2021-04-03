
-- @Title: 游戏玩法分析 I (Game Play Analysis I)
-- @Author: cocofe
-- @Date: 2021-04-03 12:35:32
-- @Runtime: 372 ms
-- @Memory: 0 B

# Write your MySQL query statement below
select player_id, min(event_date) as first_login from Activity group by player_id
