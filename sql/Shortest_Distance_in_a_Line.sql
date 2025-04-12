# Write your MySQL query statement below
select min(abs(x - next_x)) as shortest
from (
select x, lead(x) over (order by x) as next_x
from  Point) x;
