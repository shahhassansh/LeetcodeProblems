/* Write your T-SQL query statement below */
select a.name from Employee as a 
inner join (
select managerID, count(distinct id) as cnt from Employee
group by managerID
having count(distinct id) >=5) b
on b.managerID = a.id;
