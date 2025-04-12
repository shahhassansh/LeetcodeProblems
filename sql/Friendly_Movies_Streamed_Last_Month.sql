# Write your MySQL query statement below


select distinct a.title as TITLE from
Content a
left join 
TVProgram b 
on a.content_id = b.content_id
where a.Kids_content = 'Y'
and a.content_type = 'Movies'
and month(b.program_date) = '6'
and year(b.program_date) = '2020';
