select isnull(max(num),null) as num from (
select num from MyNumbers 
group by num
having count(*) = 1) t;
