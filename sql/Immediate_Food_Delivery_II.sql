with first_order as (
select customer_id, min(order_date) as order_date from Delivery
group by customer_id)
select round(sum(case when a.order_date = b.customer_pref_delivery_date 
then 100.0 else 0 end)/ count(*),2)
as immediate_percentage
from first_order as a inner join Delivery as b 
on a.customer_id = b.customer_id and a.order_date = b.order_date;
