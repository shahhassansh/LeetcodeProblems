select id, student from (
select case when id%2 = 1 and id = (select count(*) from Seat) then id
when id%2 = 1 then id+1
else id -1 end as id , student from Seat) as b
order by id asc; 
