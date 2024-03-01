with first as (select distinct * from Activities)
select sell_date, count(product) as num_sold, 
string_agg(product,',') within group (order by product) as products
from first
group by sell_date

