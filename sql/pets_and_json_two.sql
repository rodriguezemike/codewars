-- Substitute with your SQL
create function array_unique_stable(p_input anyarray)
  returns anyarray immutable strict parallel safe 
  language sql
as 
$$
select array_agg(t order by x)
from (
  select distinct on (t) t,x
  from unnest(p_input) with ordinality as p(t,x)
  order by t,x
) t2;
$$;
select
    p2.first_letter,
    p2.pet_count,
    array_to_string(array_unique_stable(array_agg(u.info->>'name' order by u.id) filter(where LEFT(pet->>'name',1) = p2.first_letter)) , ', ') user_names
from users u,
lateral jsonb_array_elements(info->'pets') as pet,
(
  select
    DISTINCT LEFT(pet->>'name', 1) first_letter,
    count(*) over (partition by LEFT(pet->>'name', 1)) as pet_count
  from users u,
  lateral jsonb_array_elements(info->'pets') as pet
) as p2
group by p2.first_letter, p2.pet_count
order by p2.pet_count desc, first_letter

