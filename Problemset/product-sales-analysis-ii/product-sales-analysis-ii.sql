
-- @Title: 产品销售分析 II (Product Sales Analysis II)
-- @Author: cocofe
-- @Date: 2021-04-03 13:19:57
-- @Runtime: 1040 ms
-- @Memory: 0 B

# Write your MySQL query statement below

select product_id, sum(quantity) as total_quantity from Sales group by product_id
