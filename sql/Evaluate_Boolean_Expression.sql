select a.*, 
case when a.operator = '>' and b.value > c.value then 'true'
when a.operator = '<' and b.value < c.value then 'true'
when a.operator = '=' and b.value = c.value then 'true'
else 'false' end as value
from Expressions a
join Variables b 
on a.left_operand = b.name
join Variables c
on a.right_operand = c.name;
