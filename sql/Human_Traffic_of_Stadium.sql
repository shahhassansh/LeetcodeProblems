/* Write your T-SQL query statement below */
select 
        a.id,
        a.visit_date,
        a.people
from Stadium a
join Stadium t
on a.id=t.id-1 
join Stadium y
on a.id=y.id-2 

where a.people >= 100  and t.people>= 100 
and y.people >= 100 

union 

select 
        a.id,
        a.visit_date,
        a.people
from Stadium a
join Stadium t
on a.id=t.id+1 
join Stadium y
on a.id=y.id-1 
where a.people >= 100  and t.people>= 100 
and y.people >= 100 

union 

select 
        a.id,
        a.visit_date,
        a.people
from Stadium a
join Stadium t
on a.id=t.id+2 
join Stadium y
on a.id=y.id+1 
where a.people >= 100  and t.people>= 100 
and y.people >= 100 




