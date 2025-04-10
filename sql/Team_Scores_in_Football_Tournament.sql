# Write your MySQL query statement below

select team_id, team_name, sum(points) as num_points from (
select a.team_id, a.team_name, 
ifnull(sum(case when b.host_goals > b.guest_goals then 3 
when b.host_goals = b.guest_goals then 1 
else 0 end),0) as points 
from Teams a
left join Matches b 
on a.team_id = b.host_team
group by 1,2
union all
select a.team_id, a.team_name, 
ifnull(sum(case when b.host_goals < b.guest_goals then 3 
when b.host_goals = b.guest_goals then 1 
else 0 end),0) as points 
from Teams a
left join Matches b 
on a.team_id = b.guest_team
group by 1,2) x
group by 1,2
order by 3 desc, 1 asc;
