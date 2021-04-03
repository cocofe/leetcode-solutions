
-- @Title: 游戏玩法分析 II (Game Play Analysis II)
-- @Author: cocofe
-- @Date: 2021-04-03 13:16:38
-- @Runtime: 379 ms
-- @Memory: 0 B

# Write your MySQL query statement below
-- select player_id, device_id from
-- (select player_id, device_id, row_number() over (partition by player_id order by event_date) as row_num from Activity) as t where t.row_num=1

-- 先找到每个用户首次登陆的时间
select Activity.player_id, device_id from Activity left join 
(select player_id, min(event_date) as min_date from Activity group by player_id) as t on  Activity.player_id = t.player_id where Activity.event_date=t.min_date
