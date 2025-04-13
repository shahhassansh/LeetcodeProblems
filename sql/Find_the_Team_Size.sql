# Write your MySQL query statement below
with team_size as
(
    select team_id, count( distinct employee_id) as team_size from  Employee
    group by 1
)
select a.employee_id, b.team_size
from Employee a
join team_size b
on a.team_id = b.team_id;

