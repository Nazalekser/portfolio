# Downloded dataset https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01
SELECT * FROM new_schema.filmlocations;
SELECT Title, Director, Writer FROM FilmLocations;
SELECT Title, ReleaseYear, Locations FROM FilmLocations WHERE ReleaseYear>=2001;
# 1. Problem
SELECT Locations, FunFacts FROM FilmLocations;
# 2. Problem
SELECT Title, ReleaseYear, Locations FROM FilmLocations where ReleaseYear<=2000;
# 3. Problem
select Title, ReleaseYear, Locations, ProductionCompany from filmlocations where Writer<>'James Cameron'