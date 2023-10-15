# Data - 3 tables:
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/MySQL/week5/chicago_public_schools.sql?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-wwwcourseraorg-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/MySQL/week5/chicago_crime.sql?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-wwwcourseraorg-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/MySQL/week5/chicago_socioeconomic_data.sql?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-wwwcourseraorg-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01

# Exercise 1: Using Joins
# 1. Write and execute a SQL query to list the school names, community names and average 
# attendance for communities with a hardship index of 98.
select CS.NAME_OF_SCHOOL, CD.COMMUNITY_AREA_NAME, CS.AVERAGE_STUDENT_ATTENDANCE
from chicago_public_schools CS
left outer join chicago_socioeconomic_data CD
on CS.COMMUNITY_AREA_NUMBER = CD.COMMUNITY_AREA_NUMBER
where CD.HARDSHIP_INDEX = '98';

# 2. Write and execute a SQL query to list all crimes that took place at a school. Include
# case number, crime type and community name.
select CC.CASE_NUMBER, CC.PRIMARY_TYPE as CRIME_TYPE, CD.COMMUNITY_AREA_NAME
from chicago_crime CC
left outer join chicago_socioeconomic_data CD
on CC.COMMUNITY_AREA_NUMBER = CD.COMMUNITY_AREA_NUMBER
where CC.LOCATION_DESCRIPTION like '%school%';

# Exercise 2: Creating a View
# - Write and execute a SQL statement to create a view showing the columns listed in the 
# following table, with new column names as shown in the second column
	# Column name in CHICAGO_PUBLIC_SCHOOLS 	Column name in view
	# NAME_OF_SCHOOL 							School_Name
	# Safety_Icon 								Safety_Rating
	# Family_Involvement_Icon 					Family_Rating
	# Environment_Icon 							Environment_Rating
	# Instruction_Icon 							Instruction_Rating
	# Leaders_Icon 								Leaders_Rating
	# Teachers_Icon 							Teachers_Rating
# - Write and execute a SQL statement that returns all of the columns from the view.
# - Write and execute a SQL statement that returns just the school name and leaders rating 
# from the view.
create view RATINGS as
select NAME_OF_SCHOOL as School_Name, Safety_Icon as Safety_Rating, 
	Family_Involvement_Icon as Family_Rating, Environment_Icon as Environment_Rating, 
	Instruction_Icon as Instruction_Rating, Leaders_Icon as Leaders_Rating, 
	Teachers_Icon as Teachers_Rating
from chicago_public_schools CS;
select * from RATINGS;
select School_Name, Leaders_Rating from RATINGS;
drop view RATINGS;

# Exercise 3: Creating a Stored Procedure
# 1. Write the structure of a query to create or replace a stored procedure called 
# UPDATE_LEADERS_SCORE that takes a in_School_ID parameter as an integer and a 
# in_Leader_Score parameter as an integer.
# 2. Inside your stored procedure, write a SQL statement to update the Leaders_Score field in
# the CHICAGO_PUBLIC_SCHOOLS table for the school identified by in_School_ID to the value in
# the in_Leader_Score parameter.
# 3. Inside your stored procedure, write a SQL IF statement to update the Leaders_Icon field in
# the CHICAGO_PUBLIC_SCHOOLS table for the school identified by in_School_ID using the 
# following information.
	# Score lower limit 	Score upper limit 	Icon
	# 80 					99 					Very strong
	# 60 					79 					Strong
	# 40 					59 					Average
	# 20 					39 					Weak
	# 0 					19 					Very weak
# 4. Run your code to create the stored procedure.
# Write a query to call the stored procedure, passing a valid school ID and a leader score of
# 50, to check that the procedure works as expected.

DELIMITER //
create procedure UPDATE_LEADERS_SCORE (
	in in_School_ID integer, in in_Leader_Score integer)
begin
	update CHICAGO_PUBLIC_SCHOOLS
	set Leaders_Score = in_Leader_Score
    where School_ID = in_School_ID;
end //
DELIMITER ;
call UPDATE_LEADERS_SCORE (610038, 50);
select School_ID, Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = 610038;
drop procedure UPDATE_LEADERS_SCORE;

alter table CHICAGO_PUBLIC_SCHOOLS
change Leaders_Icon Leaders_Icon VARCHAR(11);

DELIMITER //
create procedure UPDATE_LEADERS_SCORE (
	in in_School_ID integer, in in_Leader_Score integer)
begin
	update CHICAGO_PUBLIC_SCHOOLS
	set Leaders_Score = in_Leader_Score
    where School_ID = in_School_ID;
	if (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 80 and 90 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Very strong'
		where School_ID = in_School_ID;
	elseif (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 60 and 79 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Strong'
		where School_ID = in_School_ID;
	elseif (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 40 and 59 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Average'
		where School_ID = in_School_ID;
	elseif (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 20 and 39 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Week'
		where School_ID = in_School_ID;
	elseif (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 0 and 19 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Very week'
		where School_ID = in_School_ID;
	end if;
end //
DELIMITER ;
call UPDATE_LEADERS_SCORE (610038, 90);
select School_ID, Leaders_Score, Leaders_Icon
from CHICAGO_PUBLIC_SCHOOLS where School_ID = 610038;
drop procedure if exists UPDATE_LEADERS_SCORE;

# Exercise 4: Using Transactions
# 1. Update your stored procedure definition. Add a generic ELSE clause to the IF statement
# that rolls back the current work if the score did not fit any of the preceding categories.
DELIMITER //
create procedure UPDATE_LEADERS_SCORE (
	in in_School_ID integer, in in_Leader_Score integer)
begin
	start transaction;
	update CHICAGO_PUBLIC_SCHOOLS
	set Leaders_Score = in_Leader_Score
    where School_ID = in_School_ID;
	if (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 80 and 90 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Very strong'
		where School_ID = in_School_ID;
	elseif (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 60 and 79 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Strong'
		where School_ID = in_School_ID;
	elseif (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 40 and 59 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Average'
		where School_ID = in_School_ID;
	elseif (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 20 and 39 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Week'
		where School_ID = in_School_ID;
	elseif (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 0 and 19 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Very week'
		where School_ID = in_School_ID;
        else
        rollback;
	end if;
end //
DELIMITER ;
call UPDATE_LEADERS_SCORE (610038, 101);
select School_ID, Leaders_Score, Leaders_Icon
from CHICAGO_PUBLIC_SCHOOLS where School_ID = 610038;
drop procedure if exists UPDATE_LEADERS_SCORE;

# 2. Update your stored procedure definition again. Add a statement to commit the current
# unit of work at the end of the procedure.
DELIMITER //
create procedure UPDATE_LEADERS_SCORE (
	in in_School_ID integer, in in_Leader_Score integer)
begin
	start transaction;
	update CHICAGO_PUBLIC_SCHOOLS
	set Leaders_Score = in_Leader_Score
    where School_ID = in_School_ID;
	if (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 80 and 90 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Very strong'
		where School_ID = in_School_ID;
	elseif (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 60 and 79 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Strong'
		where School_ID = in_School_ID;
	elseif (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 40 and 59 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Average'
		where School_ID = in_School_ID;
	elseif (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 20 and 39 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Week'
		where School_ID = in_School_ID;
	elseif (select Leaders_Score from CHICAGO_PUBLIC_SCHOOLS where School_ID = in_School_ID) between 0 and 19 then
		update CHICAGO_PUBLIC_SCHOOLS
		set Leaders_Icon = 'Very week'
		where School_ID = in_School_ID;
        else
        rollback;
	end if;
    commit;
end //
DELIMITER ;
call UPDATE_LEADERS_SCORE (610038, 101);
select School_ID, Leaders_Score, Leaders_Icon
from CHICAGO_PUBLIC_SCHOOLS where School_ID = 610038;
drop procedure if exists UPDATE_LEADERS_SCORE;

# - Run your code to replace the stored procedure.
# Write and run one query to check that the updated stored procedure works as expected when
# you use a valid score of 38.
# Write and run another query to check that the updated stored procedure works as expected
# when you use an invalid score of 101.
