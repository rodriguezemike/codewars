-- https://www.codewars.com/kata/582001237a3a630ce8000a41/train/sql

-- Replace with your SQL query
select
  c.id as category_id,
  c.category,
  rp.title,
  rp.views,
  rp.id as post_id
from
  categories c left join(
  select
    row_number() over (partition by p.category_id order by views desc, id) as post_rank,
    *
  from 
    posts p) rp on rp.category_id = c.id and rp.post_rank < 3
order by
  c.category,
  rp.views desc,
  post_id
