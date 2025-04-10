# Write your MySQL query statement below
select a.name as warehouse_name, sum(ifnull(a.units * b.Width * b.Length * b.Height,0)) as volume 
from Warehouse a
left join Products b 
on a.product_id = b.product_id
group by 1;
