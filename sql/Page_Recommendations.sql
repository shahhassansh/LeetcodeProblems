# Write your MySQL query statement below
select distinct recommended_page from (

select b.page_id as recommended_page
from Friendship a
join Likes b 
on a.user2_id = b.user_id
where a.user1_id = 1

union 

select b.page_id as recommended_page
from Friendship a
join Likes b 
on a.user1_id = b.user_id
where a.user2_id = 1
) x 
where recommended_page not in (
    select page_id from Likes where user_id = 1


)

