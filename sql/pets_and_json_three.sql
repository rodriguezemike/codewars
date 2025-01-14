--https://www.codewars.com/kata/647ede2fe4d998004ad24995/train/sql

select
  case
    when cast(info->>'age' as integer) between 18 and 30 then '18-30'
    when cast(info->>'age' as integer) between 31 and 45 then '31-45'
    when cast(info->>'age' as integer) between 46 and 60 then '46-60'
    else '61 and above'
  end as "age_group",
  round(avg(jsonb_array_length(info->'pets')), 1) as avg_pet_count,
  (array_agg((users.info->>'name') order by jsonb_array_length(info->'pets') desc, id)) [1] as max_pet_owner,
  max(jsonb_array_length(info->'pets')) as max_pet_count
from users
group by age_group
order by 2 desc, 1
