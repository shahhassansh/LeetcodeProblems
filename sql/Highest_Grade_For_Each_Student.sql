# Write your MySQL query statement below
with x as 
(select student_id as xid, max(grade) as xGrade
from Enrollments
group by student_id)
select a.student_id, min(a.course_id) as course_id, a.Grade
from Enrollments as a 
join x as b 
on a.student_id = b.xid and a.Grade = b.xGrade
group by a.student_id,a.Grade
order by 1;
