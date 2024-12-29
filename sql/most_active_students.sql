-- https://www.codewars.com/kata/64a2a3d22bcea0046163eba8/train/sql

-- Substitute with your SQL
-- Unoptimized
with max_courses as (
	select c1.student_id, c1.course_name, c1.score, c1.course_date, c2.course_count, c2.course_list, row_number() over (partition by c1.student_id order by c1.score desc, c1.course_date desc, c1.course_name asc) r
	from courses c1
	join (
	  select 
	    student_id, 
	    max(score) as max_score, 
	    count(course_name) course_count,
	    array_to_string(array_agg(format('%s (%s - %s)', course_name, course_date, score) order by course_date asc, course_name asc), ', ') course_list
	  from courses
	  where course_date between '2022-10-01' and '2022-12-31'
	  group by student_id
	) c2
	on c1.student_id = c2.student_id and c1.score = c2.max_score
	where course_date between '2022-10-01' and '2022-12-31'
	order by student_id, course_date desc, course_name
)

select
  s.id as student_id,
  s.name,
  max_courses.course_count as num_courses,
  max_courses.course_name || ' (' || max_courses.score || ')' as highest_scored_course,
  max_courses.course_list
from
  students s join max_courses on max_courses.student_id = s.id
where
  r = 1
order by num_courses desc, max_courses.score desc, student_id asc
limit 20

--Optimized solution from other user

/*
-- Substitute with your SQL

select 
  student_id, 
  name, 
  count(*) num_courses,
  (array_agg(course_name order by score desc, course_date desc, course_name))[1] || ' ('||max(score)||')' highest_scored_course,
  string_agg(format('%s (%s - %s)', course_name, course_date, score), ', ' order by course_date, course_name) course_list
from
  students join courses on student_id = students.id and course_date between '2022-10-01' and '2022-12-31'
group by student_id, name
order by num_courses desc, max(score) desc, student_id
limit 20

*/
