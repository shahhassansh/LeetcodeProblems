# Write your MySQL query statement below
select customer_id, name from (
select customer_id, name, month(order_date), sum(quantity*price) from (
select a.*, b.price, c.name
from Orders a
join Product b 
join Customers c 
on a.product_id = b.product_id
and a.customer_id = c.customer_id 
where 
 month(order_date) in ('6', '7') and 
year(order_date) = '2020') x
group by 1,2,3
having sum(quantity*price) >= 100) y 
group by 1,2
having count(*) > 1
;
