/* Write your T-SQL query statement below */
select machine_id, cast(((sum(case when activity_type = 'end' then timestamp else 0 end) -  sum(case when activity_type = 'start' then timestamp 
else 0 end)) * 2) / count(*) as decimal(10,3)) as processing_time
from Activity
group by machine_id;
