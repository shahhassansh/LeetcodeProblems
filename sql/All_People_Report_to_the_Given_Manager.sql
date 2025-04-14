# Write your MySQL query statement below
with cte as 
(
select a.employee_id, a.manager_id, b.manager_id as manager2 
from  Employees a
left join Employees b
on a.manager_id = b.employee_id
)
select distinct a.employee_id
from cte a 
left join Employees b
on a.manager2 = b.employee_id
where b.manager_id = 1
and a.employee_id != 1

