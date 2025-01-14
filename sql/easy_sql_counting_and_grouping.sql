-- https://www.codewars.com/kata/594633020a561e329a0000a2/train/sql
/*  SQL  */
select
  d.race,
  count(d.race)
from
  demographics d
group by d.race
order by count(d.race) desc

