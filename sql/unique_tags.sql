--https://www.codewars.com/kata/64ce83357d57e3005885204c/train/sql

-- Substitute with your SQL
select
  row_number() over (order by count(t.tag) desc, t.tag) as tag_rank,
  t.tag,
  count(t.tag) tag_count
from
  (select
      unnest(string_to_array(tags, ',')) as tag
  from
    user_tags) as t
group by t.tag;


