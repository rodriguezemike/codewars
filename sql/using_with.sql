--https://www.codewars.com/kata/5811501c2d35672d4f000146/train/sql

-- Create your SELECT statement here
WITH special_sales as (
  SELECT
    *
  FROM
    sales
  WHERE
    price > 90.00
)

SELECT
  *
FROM
  departments
WHERE
  id IN (SELECT department_id FROM special_sales)
