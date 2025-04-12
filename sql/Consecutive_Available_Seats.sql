# Write your MySQL query statement below
-- select distinct a.seat_id 
-- from Cinema a 
-- join Cinema b 
-- on (a.seat_id = b.seat_id + 1
-- or a.seat_id = b.seat_id - 1)
-- and a.free = 1
-- and b.free = 1
-- ;

select distinct seat_id from (
select seat_id, lead(seat_id) over (order by seat_id) as next_seat,
lag(seat_id) over (order by seat_id) as prev_seat
from Cinema
where free = 1) x
where 
(seat_id + 1 = next_seat or seat_id - 1 = prev_seat);
