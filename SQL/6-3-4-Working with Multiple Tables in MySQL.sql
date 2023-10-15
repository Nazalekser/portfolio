# Exercise 1: Accessing Multiple Tables with Sub-Queries

# 1. Problem: Retrieve only the EMPLOYEES records that correspond to jobs in the JOBS table.
SELECT * from employees 
	WHERE JOB_ID in 
	(select job_ident from jobs);

# 2. Problem: Retrieve only the list of employees whose JOB_TITLE is Jr. Designer.

select * from employees 
	where JOB_ID in
	(select job_ident from jobs 
		where job_title = 'Jr. Designer');
        
# 3. Problem: Retrieve JOB information and list of employees who earn more than $70,000.

select * from JOBS 
	where JOB_IDENT IN 
    (select JOB_ID from EMPLOYEES 
		where SALARY > 70000 );

# 4. Problem: Retrieve JOB information and list of employees whose birth year is after 1976.

select * from JOBS 
	where JOB_IDENT IN 
    (select JOB_ID from EMPLOYEES 
		where year(B_DATE) > 1976);
        
# 5. Problem: Retrieve JOB information and list of female employees whose birth year is after 1976.

select * from JOBS 
	where JOB_IDENT IN 
    (select JOB_ID from EMPLOYEES 
		where year(B_DATE) > 1976 and SEX = 'F');
        
        
# Exercise 2: Accessing Multiple Tables with Implicit Joins

# 1. Problem: Perform an implicit cartesian/cross join between EMPLOYEES and JOBS tables.

select * from employees, jobs;

# 2. Problem: Retrieve only the EMPLOYEES records that correspond to jobs in the JOBS table.

select * from employees, jobs
	where employees.JOB_ID = jobs.JOB_IDENT;
    
# 3. Problem: Redo the previous query, using shorter aliases for table names.

select * from employees E, jobs J
	where E.JOB_ID = J.JOB_IDENT;
    
# 4. Problem: Redo the previous query, but retrieve only the Employee ID, Employee Name and Job Title.

select EMP_ID, F_NAME, JOB_TITLE
	from employees E, jobs J
		where E.JOB_ID = J.JOB_IDENT;
        
# 5. Redo the previous query, but specify the fully qualified column names with aliases in the SELECT clause.

select E.EMP_ID, E.F_NAME, J.JOB_TITLE
	from employees E, jobs J
		where E.JOB_ID = J.JOB_IDENT;