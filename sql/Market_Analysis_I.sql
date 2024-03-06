select a.user_id as buyer_id, a.join_date, sum(case when year(b.order_date) = '2019' then 1 else 0 end) as orders_in_2019
from Users a
left join 
Orders b
on a.user_id = b.buyer_id
group by a.user_id, a.join_date
order by a.user_id;
