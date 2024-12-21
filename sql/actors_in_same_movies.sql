-- https://www.codewars.com/kata/5817b124e7f4576fd00020a2/train/sql

select
  *
from
  (select
    f.title
  from
    film f,
    film_actor fa
  where
    f.film_id = fa.film_id and 
    fa.actor_id = 105) as sc,
  (select
    f.title
  from
    film f,
    film_actor fa
  where
    f.film_id = fa.film_id and 
    fa.actor_id = 122) as sn
where
  sc.title = sn.title;


/*
Better approach

SELECT f.title 
  FROM film f 
  INNER JOIN film_actor a ON f.film_id = a.film_id
  INNER JOIN film_actor b ON f.film_id = b.film_id
  WHERE a.actor_id = 105 AND b.actor_id = 122
  ORDER BY title;
*/
