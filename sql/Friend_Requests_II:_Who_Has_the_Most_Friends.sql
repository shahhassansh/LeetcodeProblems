with first as 
(select requester_id as id, count(*) as num from RequestAccepted 
group by requester_id
union all
select accepter_id as id, count(*) as num from RequestAccepted
group by accepter_id),
second as (
select id, sum(num) as num from first
group by id) 
select top 1 id, max(num) as num from second 
group by id
order by max(num) desc
