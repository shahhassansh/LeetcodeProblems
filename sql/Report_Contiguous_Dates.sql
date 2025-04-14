 # Write your MySQL query statement below
with cte as 
(
    select fail_date as dt, 'failed' as st 
    from Failed
    where fail_date between '2019-01-01' and '2019-12-31'
    union 
    select success_date, 'succeeded' as st 
    from Succeeded
    where success_date between '2019-01-01' and '2019-12-31'
), cte2 as (
select st, dt,
row_number() over (order by dt) - 
row_number() over(partition by st order by dt) as x
from cte
)
select st as period_state, min(dt) as start_date,
max(dt) as end_date
from cte2
group by st, x
order by 2 asc;
