select b.product_id, isnull(cast(sum(a.units * b.price)*1.0/sum(a.units) 
as DECIMAL(10,2)),0) as average_price
from UnitsSold a 
right join 
Prices b
on a.product_id = b.product_id and a.purchase_date between b.start_date 
and b.end_date
group by b.product_id;
