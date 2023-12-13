SELECT a.reports_to as employee_id, b. name, count(*) as reports_count, 
round(sum(a.age)*1.0/count(*),0) as average_age
from Employees as a
inner join Employees as b
on a.reports_to = b.employee_id
group by a.reports_to, b.name
order by employee_id;
