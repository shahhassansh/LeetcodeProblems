select a.project_id, 
isnull(cast(sum(b.experience_years)*1.0/count(experience_years) as 
decimal(10,2)),0) as average_years from
Project as a
left join Employee as b
on a.employee_id = b.employee_id
group by a.project_id;
