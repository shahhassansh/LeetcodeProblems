/* Write your T-SQL query statement below */

select a.student_id, a.student_name, b.subject_name, count(c.subject_name) as attended_exams
from Students as a cross join 
Subjects as b 
left join Examinations as c
on b.subject_name = c.subject_name
and a.student_id = c.student_id
group by a.student_id, a.student_name, b.subject_name;
