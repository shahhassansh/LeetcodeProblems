select x,y,z, case when z >= x and z>=y and x+y >z then 'Yes'
when y >=x and y >= z and x+z > y then 'Yes'
when x >=y and x >=z and y+z >x then 'Yes'
else 'No' end as triangle 
from Triangle;
