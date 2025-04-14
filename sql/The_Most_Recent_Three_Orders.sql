# Write your MySQL query statement below
select name as customer_name, customer_id, order_id, order_date
from (
select b.name, a.customer_id, a.order_id, a.order_date, row_number() over (partition by a.customer_id order by a.order_date desc) as rn 
from Orders a
join Customers b
on a.customer_id = b.customer_id) x
where rn <=3
order by 1,2 asc, 4 desc;
