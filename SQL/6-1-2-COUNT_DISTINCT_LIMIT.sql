SELECT * FROM FilmLocations;

# Exercise 1: COUNT
SELECT COUNT(*) FROM FilmLocations;
SELECT COUNT(Locations) FROM FilmLocations WHERE Writer="James Cameron";
# Practice exercises on COUNT
	# 1. Problem: Retrieve the number of locations of the films which are directed by Woody Allen.
select count(Locations) from filmlocations where Director='Woody Allen';
	# 2. Problem: Retrieve the number of films shot at Russian Hill.
select count(Title) from filmlocations where Locations='Russian Hill';
	# 3. Problem: Retrieve the number of rows having a release year older than 1950 from the "FilmLocations" table.
select count(*) from filmlocations where ReleaseYear<1950;

# Exercise 2: DISTINCT
SELECT DISTINCT Title FROM FilmLocations;
SELECT COUNT(DISTINCT ReleaseYear) FROM FilmLocations WHERE ProductionCompany="Warner Bros. Pictures";
# Practice exercises on DISTINCT
	# 1. Problem: Retrieve the name of all unique films released in the 21st century and onwards, along with their release years.
select distinct Title, ReleaseYear from filmlocations where ReleaseYear>2000;
	# 2. Problem: Retrieve the names of all the directors and their distinct films shot at City Hall.
select distinct Title, Director from filmlocations where Locations='City Hall';
	# 3. Problem: Retrieve the number of distributors distinctly who distributed films acted by Clint Eastwood as 1st actor.
select count(distinct Distributor) from filmlocations where Actor1='Clint Eastwood';

# Exercise 3: LIMIT
SELECT * FROM FilmLocations LIMIT 25;
SELECT * FROM FilmLocations LIMIT 15 OFFSET 10;
# Practice exercises on LIMIT
	# 1. Problem: Retrieve the name of first 50 films distinctly.
select distinct Title from filmlocations limit 50;
	# 2. Problem: Retrieve first 10 film names distinctly released in 2015.
select distinct Title from filmlocations where ReleaseYear=2015 limit 10;
	# 3. Problem: Retrieve the next 3 film names distinctly after first 5 films released in 2015.
select distinct Title from filmlocations where ReleaseYear=2015 limit 3 offset 5;