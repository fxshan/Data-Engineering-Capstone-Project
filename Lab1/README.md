# Exercises - Setting up the database
## Exercise 1 - Design the OLTP Database
### Task 1 - Create a database.
Use the MySQL CLI to create a datebase:  
```
CREATE DATABASE sales;
```
### Task 2 - Design a table named sales_data.
Design a table named sales_data based on the sample data given.  
<img width="398" height="156" alt="image" src="../images/sales_data.png" />  
Create the sales_data table in `sales` database:  
<img width="350px" alt="image" src="../images/1-2 createtable.png" />

# Exercises - Querying and Admin tasks
## Exercise 2 - Load the Data
### Task 3 - Import the data in the file `oltpdata.csv`.
Import the data from `oltpdata.csv` into sales_data table using phpMyAdmin.
<img width="450px" alt="image" src="../images/1-3 importdata.png" />

### Task 4 - List the tables in the database `sales`.
<img width="250px" alt="image" src="../images/1-4 listtables.png" />

### Task 5 - Write a query to find out the count of records in the tables sales_data.
<img width="350px" alt="image" src="../images/1-5 salesrows.png" />

## Exercise 3 - Set up Admin tasks
### Task 6 - Create an index.
Create an index named ts on the timestamp field.  
```CREATE INDEX ts ON sales_data(timestamp);```  

### Task 7 - List indexes.
List indexes on the table sales_data.  
<img width="1200px" alt="image" src="../images/1-7 listindexes.png" />

### Task 8 - Write a bash script to export data.
Write a bash script named `datadump.sh` that exports all the rows in the sales_data table to a file named `sales_data.sql`.
<img width="800px" alt="image" src="../images/1-8 exportdata.png" />
