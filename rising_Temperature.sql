select b.id from Weather as a 
inner join Weather as b 
on a.temperature < b.temperature and dateadd(day,1,a.recordDate) = b.recordDate;
