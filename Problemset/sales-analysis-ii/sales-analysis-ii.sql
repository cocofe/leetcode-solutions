
-- @Title: 销售分析 II (Sales Analysis II)
-- @Author: cocofe
-- @Date: 2021-04-03 17:38:23
-- @Runtime: 842 ms
-- @Memory: 0 B

# Write your MySQL query statement below

select distinct buyer_id from Sales left join Product on Sales.product_id=Product.product_id
where Product.product_name = 'S8' and buyer_id not in 
(select distinct buyer_id from Sales left join Product on Sales.product_id=Product.product_id
where Product.product_name = 'iPhone')
