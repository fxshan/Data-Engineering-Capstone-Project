# Exercise 1 - Design a Data Warehouse
The ecommerce company has provied me the sample data.  
<img width="550px" alt="image" src="images/ecom-sample-data.png" />  
Start the project by designing a Star Schema for the warehouse by identifying the columns for the various dimension and fact tables in the schema. Name the database as `softcart`.

### Task 1 - Design the dimension table `softcartDimDate`
Use the ERD design tool design the following tables. The company is looking at a granularity of a day. Which means they would like to have the ability to generate the report on yearly, monthly, daily, and weekday basis.  
Here is a partial list of fields to serve as an example:  
dateid  
month  
monthname  
…  
…  
<img width="250px" alt="image" src="images/3-1-1 softcartDimDate.png" />  
### Task 2 - Design the dimension table `softcartDimCategory`

### Task 3 - Design the dimension table `softcartDimItem`
 
### Task 4 - Design the dimension table `softcartDimCountry`
<img width="250px" alt="image" src="images/3-1-4 dimtables.png" />  

### Task 5 - Design the fact table `softcartFactSales`
<img width="250px" alt="image" src="images/3-1-5 softcartFactSales.png" />  

### Task 6 - Design the relationships
Use the ERD design tool design the required relationships(one-to-one, one-to-many etc) amongst the tables.
<img width="750px" alt="image" src="images/3-1-6 softcartRelationships.png" />  

# Exercise 2 - Create the schema
### Task 7 - Create the schema
Download the schema sql from ERD tool and create the schema in a database named `staging`.
<img width="750px" alt="image" src="images/3-1-7 createschema.png" />  

# Exercise 3 - Load Data
### Task 1 - Load data into the dimension table DimDate
<img width="850px" alt="image" src="images/3-2-1 DimDate.png" /> 

### Task 2 - Load data into the dimension table DimCategory
<img width="750px" alt="image" src="images/3-2-2 DimCategory.png" /> 

### Task 3 - Load data into the dimension table DimCountry
<img width="750px" alt="image" src="images/3-2-3 DimCountry.png" /> 

### Task 4 - Load data into the fact table FactSales
<img width="750px" alt="image" src="images/3-2-4 FactSales.png" /> 

# Exercise 4 - Queries for data analytics
### Task 5 - Create a grouping sets query
```
SELECT country, category, SUM(amount) AS totalSales
FROM "FactSales" f
LEFT JOIN "DimCountry" ct
ON f.countryid = ct.countryid
LEFT JOIN "DimCategory" cg
ON f.categoryid = cg.categoryid
GROUP BY GROUPING SETS(country, category);
```
<img width="750px" alt="image" src="images/3-2-5 groupingsets.png" /> 

### Task 6 - Create a rollup query
```
SELECT d.year, ct.country, SUM(amount) AS totalSales
FROM "FactSales" f
LEFT JOIN "DimDate" d
ON f.dateid = d.dateid
LEFT JOIN "DimCountry" ct
ON f.countryid = ct.countryid
GROUP BY ROLLUP(year, country)
ORDER BY year, country;
```
<img width="550px" alt="image" src="images/3-2-6 rollup.png" /> 

### Task 7 - Create a cube query
```
SELECT d.year, ct.country, AVG(amount) AS averageSales
FROM "FactSales" f
LEFT JOIN "DimDate" d
ON f.dateid = d.dateid
LEFT JOIN "DimCountry" ct
ON f.countryid = ct.countryid
GROUP BY CUBE(year, country)
ORDER BY year, country;
```
<img width="750px" alt="image" src="images/3-2-7 cube.png" /> 

### Task 8 - Create an MQT
```
CREATE MATERIALIZED VIEW total_sales_per_country (country, total_sales) AS
(SELECT ct.country, SUM(amount)
FROM "FactSales" f
LEFT JOIN "DimCountry" ct
ON f.countryid = ct.countryid
GROUP BY country);
```
<img width="750px" alt="image" src="images/3-2-8 mqt.png" /> 
