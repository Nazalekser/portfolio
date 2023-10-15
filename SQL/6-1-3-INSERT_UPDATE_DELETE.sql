SELECT * FROM new_schema.instructor;

INSERT INTO Instructor(ins_id, lastname, firstname, city, country)
VALUES(3, 'Saha', 'Sandip', 'Edmonton', 'CA');
INSERT INTO Instructor(ins_id, lastname, firstname, city, country)
VALUES(5, 'Doe', 'John', 'Sydney', 'AU'), (6, 'Doe', 'Jane', 'Dhaka', 'BD');
#Task: Practice exercises on INSERT
	# 1.Problem: Insert a new instructor record with id 7 for Antonio Cangiano who lives in Vancouver, 
    # CA into the "Instructor" table.
insert into Instructor(ins_id, lastname, firstname, city, country)
values(7, 'Cangiano', 'Antonio', 'Vancouver', 'CA');
	# 2.Problem: Insert two new instructor records into the "Instructor" table. First record with 
    # id 8 for Steve Ryan who lives in Barlby, GB. Second record with id 9 for Ramesh Sannareddy who 
    # lives in Hyderabad, IN.
insert into Instructor(ins_id, lastname, firstname, city, country)
values(8, 'Ryan', 'Steve', 'Barbly', 'GB'), (9, 'Ramesh', 'Sannareddy', 'Hyderabad', 'IN');

UPDATE Instructor SET city='Toronto' WHERE firstname="Sandip";
UPDATE Instructor SET city='Dubai', country='AE' WHERE ins_id=5;
# Task: Practice exercises on UPDATE
	# 1. Problem: Update the city of the instructor record to Markham whose id is 1.
update Instructor set city='Markham' where ins_id=1;
	# 2. Problem: Update the city and country for Sandip with id 4 to Dhaka and BD respectively.
update Instructor set city='Dhaka', country='BD' where ins_id=4;

DELETE FROM instructor WHERE ins_id = 6;
# Task: Practice exercise on DELETE
	# 1.Problem: Remove the instructor record of Hima.
delete from instructor where firstname='Hima';
SELECT * FROM new_schema.instructor;