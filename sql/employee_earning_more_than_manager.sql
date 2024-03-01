select name as Employee from 
(select a.*, b.salary as s2 from Employee as a 
left join Employee as b
on a.managerId = b.id) x
where salary > s2;
