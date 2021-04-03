
-- @Title: 销售员 (Sales Person)
-- @Author: cocofe
-- @Date: 2021-04-03 12:51:02
-- @Runtime: 909 ms
-- @Memory: 0 B

# Write your MySQL query statement below
select name from salesperson where sales_id not in (select distinct(orders.sales_id) from orders left join company on company.com_id=orders.com_id where company.name='RED')

