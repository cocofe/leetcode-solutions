
-- @Title: 员工奖金 (Employee Bonus)
-- @Author: cocofe
-- @Date: 2021-04-03 13:24:20
-- @Runtime: 223 ms
-- @Memory: 0 B

# Write your MySQL query statement below

select Employee.name, Bonus.bonus from Employee left join Bonus on Employee.empId=Bonus.empId
where Bonus.bonus < 1000 or Bonus.bonus is null
