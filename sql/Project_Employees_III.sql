# Write your MySQL query statement below
with cte as
(
    select a.*, b.experience_years from 
    Project a
    join Employee b 
    on a.employee_id = b.employee_id
),
cte_2 as 
(
    select project_id, max(experience_years) as experience_years from 
    cte
    group by 1
)
select a.project_id, b.employee_id
from cte_2 a
join cte b 
on a.project_id = b.project_id
and a.experience_years = b.experience_years;
