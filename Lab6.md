# Analyse search terms on the e-commerce web server
 In this assignment, I should perform a number of tasks to analyze search terms on the e-commerce web server and I should work in Watson Studio within a `Jupyter notebook` to run the analysis against a CSV file containing the webserver data. 
 Then I should load this file into a Spark data frame and print the results of the queries against this data set. 
 Lastly, I should load a pretrained sales forecasting model and use this to predict the sales for next year.

## Prepare the lab environment
1. Install spark
  ```
  !pip install pyspark
  !pip install findspark
  ```
2. Start session
  ```
  def warn(*args, **kwargs):
    pass
  import warnings
  warnings.warn = warn
  warnings.filterwarnings('ignore')
  ```
  ```
  import findspark
  findspark.init()
  
  from pyspark.sql import SparkSession
  spark = SparkSession.builder.appName('SparkML Ops').getOrCreate()
  ```
3. Download The search term dataset from the below url:  
   https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/searchterms.csv
  ```
  !wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/searchterms.csv
  ```
4. Load the csv into a spark dataframe
  ```
  df = spark.read.csv('searchterms.csv', header=True, inferSchema=True)
  ```
5. The pretrained sales forecasting model is available at  the below url:
   https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/model.tar.gz
  ```
  !wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/model.tar.gz
  !tar -xvzf model.tar.gz
  ```

### Task 1 - Print the number of rows and columns
```
rows = df.count()
cols = len(df.columns)
print((rows, cols))
```
<img width="300px" alt="image" src="images/6-1 shape.png" />

### Task 2 - Print the top 5 rows
```
df.show(5)
```
<img width="400px" alt="image" src="images/6-2 top5rows.png" />

### Task 3 - Find out the datatype of the column searchterm
```
df.schema['searchterm'].dataType
```
<img width="350px" alt="image" src="images/6-3 datatype.png" />

### Task 4 - How many times was the term `gaming laptop` searched?
```
pyspark.sql.functions import col
df.filter(col('searchterm') == 'gaming laptop').count()
```
<img width="500px" alt="image" src="images/6-4 gaminglaptop.png" />

### Task 5 - Print the top 5 most frequently used search terms
```
df.groupBy('searchterm').count().orderBy(col('count').desc()).show(5, truncate=False)
```
<img width="680px" alt="image" src="images/6-5 top5terms.png" />

### Task 6 - Load the sales forecast model
```
from pyspark.ml.regression import LinearRegressionModel
model = LinearRegressionModel.load('sales_prediction.model')
```
<img width="600px" alt="image" src="images/6-6 loadmodel.png" />

### Task 7 - Using the sales forecast model, predict the sales for the year of 2023
```
from pyspark.ml.feature import VectorAssembler

def predict(year):
    assembler = VectorAssembler(inputCols=["year"], outputCol="features")  
    df = spark.createDataFrame([(year,)],["year"])
    df_features = assembler.transform(df)
    predictions = model.transform(df_features)
    predictions.select("prediction").show()
```
```
predict(2023)
```
<img width="700px" alt="image" src="images/6-7 forecast.png" />


  
