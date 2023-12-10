select query_name, cast(avg(rating*1.0/position*1.0) as decimal(10,2)) as 
quality, 
cast(sum(case when rating < 3 then 1.0 else 0.0 end)*100.0/count(*) as 
decimal(10,2)) as poor_query_percentage
from Queries 
where query_name is not null
group by query_name;
