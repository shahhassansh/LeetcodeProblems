select request_at as Day, cast(sum(case when status != 'completed' then 1 else 0 end)*1.00/count(*) as decimal(10,2)) as "Cancellation Rate" 
from (
select a.*, b.banned as client_banned, c.banned as driver_banned from
Trips as a
left join  Users as b 
on a.client_id = b.users_id
left join Users as c 
on a.driver_id = c.users_id) x
where client_banned = 'No' and driver_banned = 'No'
and request_at between '2013-10-01' and '2013-10-03'
group by request_at;
