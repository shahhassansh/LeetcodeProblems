# Write your MySQL query statement below
with first as (
select player_id, min(event_date) as event_date
from Activity
group by 1)
select a.player_id, a.device_id
from Activity a
join first b 
on a.player_id = b.player_id and a.event_date = b.event_date;
