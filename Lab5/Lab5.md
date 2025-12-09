# Part 1: ETL
## Prepare the lab environment
Before you start the assignment:  
1. Start MySQL server
2. Create a database named `sales`
3. Download the file `sales.sql`
4. Import the data in the file `sales.sql` into the `sales` database
5. Download the `mysqlconnect.py` python programs. `mysqlconnect.py` has the sample code to help to understand how to connect to MySQL using Python.
6. Modify `mysqlconnect.py` suitably and make sure I'm able to connect to the MySQL server instance on the Theia environment
7. Download the `postgresqlconnect.py` python program. `postgresqlconnect.py` has the sample code to help to understand how to connect to the PostgreSql data warehouse using Python.  
  ```python3 -m pip install psycopg2```
8. Modify `postgresqlconnect.py` suitably and make sure you are able to connect to PostgreSql from the Theia environment.
9. Download the file `sales.csv`
10. Create a table called `sales_data` using the columns `rowid`, `product_id`, `customer_id`, `price`, `quantity`, `timeestamp`. Load `sales.csv` into the table `sales_data` on your PostgreSql database.
11. Download the `automation.py`, which is used as a scafolding program to execute the tasks in this assignment.

## Exercise 1 - Automate loading of incremental data into the data warehouse
One of the routine tasks that is carried out around a data warehouse is the extraction of daily new data from the operational database and loading it into the data warehouse. 
In this exercise the extraction of incremental data should be automated, and be loaded into the data warehouse.  

### Task 1 - Implement the function `get_last_rowid()`
This function must connect to the PostgreSql as the data warehouse and return the last rowid.  
<img width="600px" alt="image" src="images/5-1-1 get_last_rowid.png" />

### Task 2 - Implement the function `get_latest_records()`
In the program `automation.py` implement the function `get_latest_records()`.  
This function must connect to the MySQL database and return all records later than the given `last_rowid`.
<img width="600px" alt="image" src="images/5-1-2 get_latest_record.png" />

### Task 3 - Implement the function `insert_records()`
In the program `automation.py` implement the function `insert_records()`.  
This function must connect to the PostgreSQL data warehouse and insert all the given records.
<img width="600px" alt="image" src="images/5-1-3 insert_records.png" />

### Task 4 - Test the data synchronization
Run the program `automation.py` and test if the synchronization is happening as expected.  
<img width="600px" alt="image" src="images/5-1-4 synchronization.png" />

# Part 2: Data Pipelines Using Apache AirFlow
## Exercise 2 - Create a DAG
### Task 1 - Define the DAG arguments
Create a DAG with these arguments:  
- owner
- start_date
- email
<img width="500px" alt="image" src="images/5-2-1 dag_args.png" />

### Task 2 - Define the DAG
Create a DAG named `process_web_log` that runs daily.  
<img width="500px" alt="image" src="images/5-2-2 dag_definition.png" />

### Task 3 - Create a task to extract data
Create a task named `extract_data`.  
This task should extract the ipaddress field from the web server log file and save it into a file named `extracted_data.txt`.  
<img width="600px" alt="image" src="images/5-2-3 extract_data.png" />

### Task 4 - Create a task to transform the data in the txt file
Create a task named `transform_data`.  
This task should filter out all the occurrences of ipaddress “198.46.149.143” from `extracted_data.txt` and save the output to a file named `transformed_data.txt`.  
<img width="700px" alt="image" src="images/5-2-4 transform_data.png" />

### Task 5 - Create a task to load the data
Create a task named `load_data`.  
This task should archive the file `transformed_data.txt` into a tar file named `weblog.tar`.  
<img width="700px" alt="image" src="images/5-2-5 load_data.png" />

### Task 6 - Define the task pipeline
Define the task pipeline as per the details given below:  
| Task  | Functionality |
| ------------- | ------------- |
| First task  | `extract_data`  |
| Second task  | `transform_data`  |
| Third task | `load_data` |
<img width="400px" alt="image" src="images/5-2-6 pipeline.png" />

## Exercise 3 - Getting the DAG operational
### Task 7 - Submit the DAG
<img width="900px" alt="image" src="images/5-2-7 submit_dag.png" />

### Task 8 - Unpause the DAG
<img width="1000px" alt="image" src="images/5-2-8 unpause_dag.png" />

### Task 9 - Monitor the DAG
<img width="800px" alt="image" src="images/5-2-9 dag_runs.png" />
