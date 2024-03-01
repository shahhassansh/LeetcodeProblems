CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
      select salary as getNthHighestSalary from 
       (select id, salary, dense_rank() over (order by salary desc) as rn from Employee) b
       where rn = @N group by salary


    );
END
