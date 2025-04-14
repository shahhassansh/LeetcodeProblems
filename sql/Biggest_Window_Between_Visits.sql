# Write your MySQL query statement below

with cte0 as
(
select distinct user_id, '2021-01-01' as visit_date
from UserVisits 
union 
select * from UserVisits
),
cte as 
(
select user_id, visit_date, 
lag(visit_date) over (partition by user_id order by visit_date) as prev 
from cte0
)
select user_id, max(datediff(visit_date, prev)) as biggest_window
from cte
group by 1
