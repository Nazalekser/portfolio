# Data - 3 tables:
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/MySQL/week5/chicago_public_schools.sql?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-wwwcourseraorg-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/MySQL/week5/chicago_crime.sql?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-wwwcourseraorg-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/MySQL/week5/chicago_socioeconomic_data.sql?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-wwwcourseraorg-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01

# 1. List the case number, type of crime and community area for all crimes in community area
# number 18.
select CC.CASE_NUMBER, CC.PRIMARY_TYPE as CRIME_TYPE, CD.COMMUNITY_AREA_NUMBER
from chicago_crime CC
inner join chicago_socioeconomic_data CD
on CC.COMMUNITY_AREA_NUMBER = CD.COMMUNITY_AREA_NUMBER
where CD.COMMUNITY_AREA_NUMBER = '18';

# 2. List all crimes that took place at a school. Include case number, crime type and 
# community name.
select CC.CASE_NUMBER, CC.PRIMARY_TYPE as CRIME_TYPE, CD.COMMUNITY_AREA_NAME
from chicago_crime CC
left outer join chicago_socioeconomic_data CD
on CC.COMMUNITY_AREA_NUMBER = CD.COMMUNITY_AREA_NUMBER
where CC.LOCATION_DESCRIPTION like '%school%';

# 3. For the communities of Oakland, Armour Square, Edgewater and CHICAGO list the 
# associated community_area_numbers and the case_numbers.

select CD.COMMUNITY_AREA_NAME, CD.COMMUNITY_AREA_NUMBER, CC.CASE_NUMBER
from chicago_crime CC
right outer join chicago_socioeconomic_data CD
on CC.COMMUNITY_AREA_NUMBER = CD.COMMUNITY_AREA_NUMBER
where CD.COMMUNITY_AREA_NAME in('Oakland', 'Armour Square', 'Edgewater', 'CHICAGO')
union
select CD.COMMUNITY_AREA_NAME, CD.COMMUNITY_AREA_NUMBER, CC.CASE_NUMBER
from chicago_crime CC
left outer join chicago_socioeconomic_data CD
on CC.COMMUNITY_AREA_NUMBER = CD.COMMUNITY_AREA_NUMBER
where CD.COMMUNITY_AREA_NAME in('Oakland', 'Armour Square', 'Edgewater', 'CHICAGO');