# Write your MySQL query statement below
select player_id, player_name, sum(total_slams) as grand_slams_count
from (

select a.player_id, a.player_name, count(*) as total_slams 
from Players a
join Championships b 
on 
a.player_id = b.wimbledon
group by a.player_name

union all

select a.player_id, a.player_name, count(*) as total_slams 
from Players a
join Championships b 
on 
a.player_id = b.Fr_open
group by a.player_name

union all

select a.player_id, a.player_name, count(*) as total_slams 
from Players a
join Championships b 
on 
a.player_id = b.US_open
group by a.player_name

union all

select a.player_id, a.player_name, count(*) as total_slams 
from Players a
join Championships b 
on 
a.player_id = b.Au_open
group by a.player_name
) x
group by 1,2
