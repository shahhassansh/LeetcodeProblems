with x as 
(select product_id, min(year) as first_year from Sales
group by product_id)
select a.product_id, a.first_year, b.quantity, b.price 
from x as a inner join Sales as b 
on a.product_id = b.product_id and a.first_year = b.year;
