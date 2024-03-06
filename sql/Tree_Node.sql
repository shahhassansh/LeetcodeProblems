select id, 'Root' as type from Tree where p_id is null
union all
select id, 'Leaf' from Tree where p_id is not null and id not in (select p_id from Tree where p_id is not null)
union all
select id, 'Inner' from Tree where p_id is not null and id in (select p_id from Tree where p_id is not null);

