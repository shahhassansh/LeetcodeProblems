select contest_id , cast(count(*)*100.0/(select count(*) from Users) as 
Decimal(10,2)) as percentage
from Register 
group by contest_id
order by percentage desc, contest_id;
