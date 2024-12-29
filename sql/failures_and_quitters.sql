--https://www.codewars.com/kata/64956edc8673b3491ce5ad2c/train/sql

with quitters as (
  select s.id as student_id, s.name, 0 failed_courses,'quit studying' reason
  from
    students s
  where
    s.id not in (select student_id from courses)),
failures as (
  select c.student_id as student_id, s.name, count(*) failed_courses, 'failed in ' || string_agg(format('%s(%s)', c.course_name, c.score), ', ' order by c.course_name) reason
  from
    courses c, students s
  where
    c.score < 60 and c.student_id = s.id
  group by c.student_id, s.name)

select student_id, name, reason from quitters
union all
  select student_id, name, reason from failures
where failed_courses = 0 or failed_courses >= 3
order by student_id

-- More typical solution (synthesized with another solution)

/*

-- Substitute with your SQL
select 
  s.id as student_id, 
  s.name,
  case
    when count(c.id)= 0 then 'quit studying'
    else 'failed in ' || string_agg(format('%s(%s)', c.course_name, c.score), ', ' order by c.course_name) 
  end as reason
from students s
left outer join courses c on c.student_id = s.id
where c.student_id is null or c.score < 60
group by s.id, s.name
having count(c.id) = 0 or count(c.id) >= 3
order by s.id;

*/

