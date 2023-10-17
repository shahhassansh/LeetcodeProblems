/* Write your T-SQL query statement below */
select a.user_id, cast((sum(case when b.action = 'confirmed' then 1 else 0 end)*1.0)/count(*) as Decimal(10,2)) as confirmation_rate
from
Signups as a 
left join Confirmations as b 
on a.user_id = b.user_id
group by a.user_id;
