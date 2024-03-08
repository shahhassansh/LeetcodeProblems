select name, travelled_distance from (
select b.id,b.name, isnull(sum(a.distance),0) as travelled_distance
from Rides a
right join Users b 
on a.user_id = b.id
group by b.id,b.name) x
order by travelled_distance desc;
