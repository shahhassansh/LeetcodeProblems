select b.name, sum(a.amount) as balance 
from Transactions as a 
right join Users as b 
on a.account = b.account
group by b.name
having sum(a.amount) > 10000; 
