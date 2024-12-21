--https://www.codewars.com/kata/581676828906324b8b00059e/train/sql


-- Create your SELECT statement here
select
  *
from
  product
where 
  to_tsvector(name) @@ to_tsquery('Awesome');
