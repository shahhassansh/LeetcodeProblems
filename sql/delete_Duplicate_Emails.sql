with a as (
select min(id) as id, email from Person
group by email )
delete from Person where id not in (select id from a);
