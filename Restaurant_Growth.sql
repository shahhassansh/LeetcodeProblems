DECLARE @START_DATE DATE;
DECLARE @END_DATE DATE;

SELECT @START_DATE = MIN(visited_on),
      @END_DATE = MAX(visited_on)
FROM Customer;

WITH date_cte AS
(
SELECT @START_DATE  AS visited_on
UNION ALL
SELECT DATEADD(DAY,1,visited_on)
FROM date_cte
WHERE visited_on < @END_DATE
)

select * from (
SELECT   d.visited_on, 
         SUM(SUM(amount)) OVER(ORDER BY d.visited_on ROWS BETWEEN 6 
PRECEDING AND CURRENT ROW)   AS'amount',
         ROUND(CAST(SUM(SUM(amount)) OVER(ORDER BY d.visited_on ROWS 
BETWEEN 6 PRECEDING AND CURRENT ROW) AS FLOAT)/7.0 ,2) 
AS'average_amount' 
FROM     Customer as c
right join date_cte as d
on c.visited_on = d.visited_on
GROUP BY d.visited_on
ORDER BY d.visited_on
 OFFSET 6 ROWS ) x
 where x.visited_on in (select visited_on from Customer)
