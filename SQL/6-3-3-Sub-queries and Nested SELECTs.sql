# 1. Problem: Execute a failing query (i.e. one which gives an error) to retrieve all 
# employees records whose salary is lower than the average salary.

select * 
from employees 
where salary < avg(salary);

# 2. Problem: Execute a working query using a sub-select to retrieve all employees records 
# whose salary is lower than the average salary.

select * 
from employees 
where salary < (select avg(salary) from employees);

# 3. Problem: Execute a failing query (i.e. one which gives an error) to retrieve all
# employees records with EMP_ID, SALARY and maximum salary as MAX_SALARY in every row.

select emp_id, salary, max(salary) as MAX_SALARY
from employees;

# 4. Problem: Execute a Column Expression that retrieves all employees records with 
# EMP_ID, SALARY and maximum salary as MAX_SALARY in every row.

select emp_id, salary, (select max(salary) from employees) as MAX_SALARY
from employees;

# 5. Problem: Execute a Table Expression for the EMPLOYEES table that excludes columns with 
# sensitive employee data (i.e. does not include columns: SSN, B_DATE, SEX, ADDRESS, SALARY).

select *
from (select emp_id, f_name, l_name, job_id, manager_id, dep_id 
		from employees) as EMP4ALL;