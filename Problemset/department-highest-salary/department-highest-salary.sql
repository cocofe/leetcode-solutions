
-- @Title: 部门工资最高的员工 (Department Highest Salary)
-- @Author: cocofe
-- @Date: 2021-04-04 16:52:29
-- @Runtime: 449 ms
-- @Memory: 0 B

# Write your MySQL query statement below

select Department.name as Department, t.Name as Employee, t.Salary from 
(select DepartmentId, Name, Salary, rank() over (partition by DepartmentId order by Salary desc) as _rank from Employee) as t right join Department on t.DepartmentId=Department.Id
where t._rank=1


