/*
SQL Basics: Create a FUNCTION (DATES)


For this challenge you need to create a basic Age Calculator function which calculates the age in years on the age field of the peoples table.

The function should be called agecalculator, it needs to take 1 date and calculate the age in years according to the date NOW and must return an integer.

You may query the people table while testing but the query must only contain the function on your final submit.

people table schema
id
name
age
NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.

Solution seems to be off by 1 for some queries


-- Create your FUNCTION statement here
CREATE FUNCTION agecalculator(some_date DATE) RETURNS INT
LANGUAGE PLPGSQL
AS $$
  DECLARE
    NOW DATE;
  BEGIN
    SELECT CURRENT_DATE
    INTO NOW;
    
    RETURN EXTRACT(YEAR FROM NOW) - EXTRACT(YEAR FROM some_date);
  END;
$$
Didnt know about the AGE function
*/

CREATE FUNCTION agecalculator(age DATE) RETURNS INTEGER AS $$
BEGIN
    return date_part('year', AGE(age));
END 
$$ LANGUAGE plpgsql;

