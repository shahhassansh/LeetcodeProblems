with distinct_product as 
(select distinct product_id from Products),
first_table as (
select product_id, max(change_date) as the_date
from Products
where change_date <= '2019-08-16'
group by product_id),
final_table as (
select a.product_id, a.new_price 
from Products as a
left join first_table as b
on a.product_id = b.product_id and a.change_date = b.the_date
where b.the_date is not null)
select a.product_id, isnull(b.new_price,10) as price 
from distinct_product as a 
left join final_table as b 
on a.product_id = b.product_id;
