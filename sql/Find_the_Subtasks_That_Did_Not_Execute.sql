# Write your MySQL query statement below
with recursive cte as (
select task_id, subtasks_count as subtask_id from 
Tasks
union 
select task_id, (subtask_id -1) as subtask_id from 
cte 
where subtask_id >1 
)
select * from cte
where (task_id, subtask_id) not in 
(select task_id, subtask_id from Executed)
