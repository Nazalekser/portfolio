# 1. Select the names and job start dates of all employees who work for the department number 5.
select F_NAME, L_NAME, START_DATE
from employees E
inner join job_history J
on E.EMP_ID = J.EMPL_ID
where E.DEP_ID = 5;

# 2. Select the names, job start dates, and job titles of all employees who work for the 
# department number 5.
select E.F_NAME, E.L_NAME, JH.START_DATE, J.JOB_TITLE
from employees E
inner join job_history JH on E.EMP_ID = JH.EMPL_ID
inner join jobs J on E.JOB_ID = J.JOB_IDENT
where E.DEP_ID = 5;

# 3. Perform a Left Outer Join on the EMPLOYEES and DEPARTMENT tables and select employee id,
# last name, department id and department name for all employees.
select E.EMP_ID, E.L_NAME, E.DEP_ID, D.DEP_NAME
from employees E
left outer join departments D
on E.DEP_ID = D.DEPT_ID_DEP;

# 4. Re-write the previous query but limit the result set to include only the rows for 
# employees born before 1980.
select E.EMP_ID, E.L_NAME, E.DEP_ID, D.DEP_NAME
from employees E
left outer join departments D
on E.DEP_ID = D.DEPT_ID_DEP
where year(E.B_DATE) < 1980;

# 5. Re-write the previous query but have the result set include all the employees but 
# department names for only the employees who were born before 1980.
select E.EMP_ID, E.L_NAME, E.DEP_ID, D.DEP_NAME
from employees E
left outer join departments D
on E.DEP_ID = D.DEPT_ID_DEP
and year(E.B_DATE) < 1980;

# 6. Perform a Full Join on the EMPLOYEES and DEPARTMENT tables and select the First name, 
# Last name and Department name of all employees.
select E.F_NAME, E.L_NAME, D.DEP_NAME
from employees E 
left outer join departments D
on E.DEP_ID = D.DEPT_ID_DEP
UNION
select E.F_NAME, E.L_NAME, D.DEP_NAME
from employees E 
right outer join departments D
on E.DEP_ID = D.DEPT_ID_DEP;

# 7. Re-write the previous query but have the result set include all employee names but 
# department id and department names only for male employees.
select E.F_NAME, E.L_NAME, D.DEP_NAME, D.DEPT_ID_DEP
from employees E 
left outer join departments D
on E.DEP_ID = D.DEPT_ID_DEP
and E.SEX = 'M'
UNION
select E.F_NAME, E.L_NAME, D.DEP_NAME, D.DEPT_ID_DEP
from employees E 
right outer join departments D
on E.DEP_ID = D.DEPT_ID_DEP
and E.SEX = 'M';