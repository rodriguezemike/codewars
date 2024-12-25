--https://www.codewars.com/kata/5ab828bcedbcfc65ea000099/train/sql
select
  pokemon_name,
  str*multiplier as modifiedStrength,
  element
from
    pokemon,
    multipliers
where
  pokemon.element_id = multipliers.id and str*multiplier >= 40
order by modifiedStrength desc;
