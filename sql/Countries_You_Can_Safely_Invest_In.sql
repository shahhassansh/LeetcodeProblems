# Write your MySQL query statement below
with first as (
select a.duration, c.name as country
from Calls a
join Person b
on a.caller_id = b.id or a.callee_id = b.id
join Country c
on substring(b.phone_number,1,3) = c.country_code)
select country
from first 
group by country
having avg(duration) > (select avg(duration) from first)



