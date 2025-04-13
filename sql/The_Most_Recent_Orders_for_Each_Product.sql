# Write your MySQL query statement below
with first as 
(
    select a.product_id, b.product_name, max(a.order_date) as order_date 
    from Orders a 
    join Products b 
    on a.product_id = b.product_id
    group by 1
)
select a.product_name, a.product_id, b.order_id, a.order_date
from first a
join Orders b 
on a.product_id = b.product_id and a.order_date = b.order_date
order by 1,2,3 asc;
