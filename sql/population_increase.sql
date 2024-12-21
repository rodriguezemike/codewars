-- https://www.codewars.com/kata/6448fccc02d9290024ee766f/train/sql

select
  p2.country,
  to_char(round((p2.population - p1.population)*1.0/1000000.0,2),'FM999999999.00') || ' M' as population_increase
from
  world_population p2,
  world_population p1
where
  p2.country = p1.country and p1.year = 2000 and p2.year = 2020
order by
  p2.population - p1.population desc
limit 5;
