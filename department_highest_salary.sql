select x.name as Department, y.name as Employee, y.salary as Salary from (
select a.name, a.departmentId, a.salary from Employee as a
inner join 
(select departmentID, max(salary) as m_sal
from Employee
group by departmentID) as b 
on a.departmentId = b.departmentID and a.salary = b.m_sal) as y
inner join Department as x 
on x.id = y.departmentId;
