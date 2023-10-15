# Exercise 1: String Patterns

# 1. Problem: Retrieve all employees whose address is in Elgin,IL.
select F_NAME, L_NAME
FROM employees
WHERE ADDRESS like '%Elgin,IL%';

# 2. Problem: Retrieve all employees who were born during the 1970's.
select f_name, l_name
from employees
WHERE B_DATE like '197%';

# 3. Problem: Retrieve all employees in department 5 whose salary is between 60000 and 70000.
select F_NAME, L_NAME, SALARY
from employees
where DEP_ID = 5 and (SALARY between 60000 and 70000);

# Exercise 2: Sorting

# 1. Problem: Retrieve a list of employees ordered by department ID.
select f_name, l_name, DEP_ID
from employees
order by DEP_ID;

# 2. Problem: Retrieve a list of employees ordered in descending order by department ID and within each department ordered alphabetically in descending order by last name.
select f_name, l_name, DEP_ID
from employees
order by DEP_ID desc, l_name desc;

# 3. (Optional) Problem: In SQL problem 2 (Exercise 2 Problem 2), use department name instead of department ID. Retrieve a list of employees ordered by department name, 
# and within each department ordered alphabetically in descending order by last name.
select f_name, l_name, DEP_ID
from employees
order by DEP_ID desc, l_name desc;

# Exercise 3: Grouping

# 1. Problem: For each department ID retrieve the number of employees in the department.
select DEP_ID, COUNT(*)
from employees
GROUP BY DEP_ID;

# 2. Problem: For each department retrieve the number of employees in the department, and the average employee salary in the department.
select DEP_ID, COUNT(*), AVG(salary)	# or COUNT(DEP_ID)
from employees
GROUP BY (DEP_ID);

# 3. Problem: Label the computed columns in the result set of SQL problem 2 (Exercise 3 Problem 2) as NUM_EMPLOYEES and AVG_SALARY.
select DEP_ID, COUNT(*) as NUM_EMPLOYEES, AVG(salary) as AVG_SALARY
from employees
GROUP BY (DEP_ID);

# 4. Problem: In SQL problem 3 (Exercise 3 Problem 3), order the result set by Average Salary.
select DEP_ID, COUNT(*) as NUM_EMPLOYEES, AVG(salary) as AVG_SALARY
from employees
GROUP BY (DEP_ID)
order by AVG_SALARY;

# 5. Problem: In SQL problem 4 (Exercise 3 Problem 4), limit the result to departments with fewer than 4 employees.
select DEP_ID, COUNT(*) as NUM_EMPLOYEES, AVG(salary) as AVG_SALARY
from employees
GROUP BY (DEP_ID)
having count(*) < 4		# or COUNT(DEP_ID)
order by AVG_SALARY;