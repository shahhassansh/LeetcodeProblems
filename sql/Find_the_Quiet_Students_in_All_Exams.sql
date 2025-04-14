# Write your MySQL query statement below
with cte as 
(
    select exam_id, min(score) as lo, max(score) as hh
    from Exam
    group by 1
),
cte2 as (
select a.student_id
from Exam a
join cte b 
on a.exam_id = b.exam_id and (a.score = b. lo or a.score = b.hh)),
cte3 as (
select * from Student 
where student_id in (select student_id from Exam))
select * from cte3
where student_id not in (select student_id from cte2)

