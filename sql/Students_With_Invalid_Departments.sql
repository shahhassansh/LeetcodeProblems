# Write your MySQL query statement below
select distinct id, name from Students
where department_id not in 
(select id from Departments)
