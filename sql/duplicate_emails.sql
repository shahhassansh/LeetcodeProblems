select email as Email from
(select email, count(*) as cnt from Person
group by email
having count(*) >1) b;
