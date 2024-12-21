--https://www.codewars.com/kata/5ca6c0a2783dec001da025ee/train/sql

--# write your SQL statement here: 
-- you are given a table 'numblocks' with columns 'w', 'l' and 'h' (the bounds in SQL translation: 1 <= w,l,h <= 10^5)
-- return a table with all these columns and your result in a column named 'res'.

create or replace function calc_pyramid(w bigint, l bigint, h bigint) returns bigint as $$
  declare
    blocks bigint = 0;
  begin
    while h > 0 loop
      blocks = blocks + (w*l);
      w = w + 1;
      l = l + 1;
      h = h - 1;
    end loop;
  return blocks;
  end;
$$ language plpgsql;

select
  w,
  l,
  h,
  calc_pyramid(w,l,h) as res
from
  numblocks;
