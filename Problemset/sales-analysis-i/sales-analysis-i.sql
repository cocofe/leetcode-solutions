
-- @Title: 销售分析 I  (Sales Analysis I)
-- @Author: cocofe
-- @Date: 2021-04-03 17:25:02
-- @Runtime: 788 ms
-- @Memory: 0 B

# Write your MySQL query statement below

select seller_id from Sales group by  seller_id having sum(price) in (
    select max(total_price) as max_price from 
(select sum(price) as total_price, seller_id from Sales group by seller_id) as t
) 

