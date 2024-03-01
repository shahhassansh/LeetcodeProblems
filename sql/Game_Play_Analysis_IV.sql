/* Write your T-SQL query statement below */

with a as 
(select player_id, min(event_date) as first_login from Activity
group by player_id)
select cast(count(distinct x.player_id)*1.00/(select count(distinct player_id) from Activity) as decimal(10,2))
as fraction from 
Activity as x
inner join a
on x.event_date = dateadd(day,1,a.first_login) and a.player_id = x.player_id;
