with first as 
(select a.*,b.name, c.title from MovieRating as a
left join Users as b on a.user_id = b.user_id
left join Movies as c on a.movie_id = c.movie_id),
second as (
select top 1 name, count(*) as no_rating from first 
group by name 
order by no_rating desc, name asc ),
third as (
select top 1 title, (sum(rating)*1.0)/count(*) as avg_rating from first 
where month(created_at) = 2 and year(created_at) = 2020
group by title
order by avg_rating desc, title asc) 
select name as results from second  union all
select title from third ;
