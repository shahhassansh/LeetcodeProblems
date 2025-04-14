# Write your MySQL query statement below
with cte as 
(
    select a.customer_id, a.product_id, b.product_name, count(*) as freq
    from Orders a
    join Products b
    on a.product_id = b.product_id
    group by 1,2,3
),
cte2 as 
(
    select customer_id, max(freq) as freq
    from cte
    group by 1
)
select a.customer_id, a.product_id, a.product_name
from cte a 
join cte2 b 
on a.customer_id = b.customer_id
and a.freq = b.freq;
