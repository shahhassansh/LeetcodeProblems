select y.name as Department, x.name as Employee, x.salary as Salary
from (
select departmentId, name, salary from (
select name,departmentId,salary,  dense_rank() over (partition by departmentId order by salary desc) as rk
from Employee) a where rk <=3) x
inner join Department as y
on x.departmentId = y.id;
