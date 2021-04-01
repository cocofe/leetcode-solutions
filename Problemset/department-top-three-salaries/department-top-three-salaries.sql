
-- @Title: 部门工资前三高的所有员工 (Department Top Three Salaries)
-- @Author: cocofe
-- @Date: 2021-02-09 21:19:02
-- @Runtime: 521 ms
-- @Memory: 0 B

# Write your MySQL query statement below

select Department.Name as Department, Employee.Name as Employee, Employee.Salary from Employee join Department on Employee.DepartmentId=Department.Id where Employee.Id in (
    select e1.Id from Employee as e1 left join Employee as e2 on e1.DepartmentId=e2.DepartmentId and e2.Salary > e1.Salary group by e1.Id having count(distinct e2.Salary) <= 2
)

-- select e1.Id, count(e2.Salary) from Employee as e1 left join Employee as e2 on e1.DepartmentId=e2.DepartmentId where e2.Salary > e1.Salary group by e1.Id having count(distinct e2.Salary) <= 2
