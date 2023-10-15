# Exercise 1: Aggregate Functions

# Query A1: Enter a function that calculates the total cost of all animal rescues in the PETRESCUE table.
select SUM(saleprice) 
from petsale;

# Query A2: Enter a function that displays the total cost of all animal rescues in the PETRESCUE table in a column called SUM_OF_COST.
select SUM(saleprice) as SUM_OF_COST
from petsale;

# Query A3: Enter a function that displays the maximum quantity of animals rescued.
select MAX(quantity)
from petsale;

# Query A4: Enter a function that displays the average cost of animals rescued.
select AVG(saleprice)
from petsale;

# Query A5: Enter a function that displays the average cost of rescuing a dog.
select AVG(saleprice/QUANTITY)
from petsale
WHERE ANIMAL = 'Dog';


# Exercise 2: Scalar and String Functions

# Query B1: Enter a function that displays the rounded cost of each rescue.
select round(saleprice) from petsale;

# Query B2: Enter a function that displays the length of each animal name.
select length(animal) from petsale;

# Query B3: Enter a function that displays the animal name in each rescue in uppercase.
select ucase(animal) from petsale;

# Query B4: Enter a function that displays the animal name in each rescue in uppercase without duplications.
select distinct(ucase(animal)) from petsale;

#Query B5: Enter a query that displays all the columns from the PETRESCUE table, where the animal(s) rescued are cats. Use cat in lower case in the query.
select * from petsale where lcase(animal) = 'cat';


# Exercise 3: Date and Time Functions

# Query C1: Enter a function that displays the day of the month when cats have been rescued.
select day(saledate) from petsale;

# Query C2: Enter a function that displays the number of rescues on the 5th month.
select quantity from petsale WHERE month(SALEDATE) = 5;

# Query C3: Enter a function that displays the number of rescues on the 14th day of the month.
select quantity from petsale where day(saledate) = 14;

# Query C4: Animals rescued should see the vet within three days of arrivals. Enter a function that displays the third day from each rescue.
select (saledate + INTERVAL 3 DAY) from petsale;

# Query C5: Enter a function that displays the length of time the animals have been rescued; the difference between todayâ€™s date and the rescue date.
select datediff(current_date, saledate) from petsale;
select (current_date - saledate) from petsale;