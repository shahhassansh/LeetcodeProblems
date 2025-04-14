# Write your MySQL query statement below
with cte as 
(
    select cast(day as date) dt, max(amount) as tn 
    from Transactions
    group by 1
)

select b.transaction_id 
from cte a 
join Transactions b
on a.dt = cast(b.day as date) and a.tn = b.amount
order by 1 asc;
