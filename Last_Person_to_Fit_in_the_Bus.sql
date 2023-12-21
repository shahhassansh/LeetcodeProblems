select top 1 person_name from (
select person_name, sum(weight) over (order by turn asc) as moving_sum
from Queue ) as b
where moving_sum <= 1000
order by moving_sum desc;
