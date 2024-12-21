--https://www.codewars.com/kata/64775418ac16620042e2efce

-- Substitute with your SQL

with user_pets as(
  select
    u.id,
    u.info->'name'#>> '{}' user_name,
    array_to_string(array_agg(p->'name'#>> '{}') filter(where p->'name'#>> '{}' like 'M%'), ', ') pet_names
  from 
    users u
  cross join jsonb_array_elements(u.info->'pets') as p
  group by u.id)
  
select *
from user_pets
where pet_names is not null;

/*
Short hand

select id, info->>'name' as user_name, string_agg(pet->>'name', ', ') as pet_names
from users, jsonb_array_elements(info->'pets') as pet
where pet->>'name' like 'M%'
group by id
order by id

*/
