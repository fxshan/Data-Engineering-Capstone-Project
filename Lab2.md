# Exercise - Working with MongoDB
### Task 1 - Import ‘catalog.json’ into mongodb server into a database named ‘catalog’ and a collection named ‘electronics’
```mongoimport -u root -p <yourpassword> --authenticationDatabase admin --db catalog --collection electronics --file catalog.json --host mongo```  
<img width="650px" alt="image" src="images/2-1 mongoimport.png" />

### Task 2 - List out all the databases
<img width="180px" alt="image" src="images/2-2 list-dbs.png" />

### Task 3 - List out all the collections in the database `catalog`
<img width="300px" alt="image" src="images/2-3 list-collections.png" />

### Task 4 - Create an index on the field “type”
<img width="450px" alt="image" src="images/2-4 create-index.png" />

### Task 5 - Write a query to find the count of laptops
```db.electronics.countDocuments({'type':'laptop'})```  
<img width="550px" alt="image" src="images/2-5 mongo-query-laptops.png" />

### Task 6 - Write a query to find the number of smart phones with screen size of 6 inches
```
db.electronics.countDocuments({'type':'smart phone',
                               'screen size':6})
```  
<img width="650px" alt="image" src="images/2-6 mongo-query-mobiles1.png" />

### Task 7 - Write a query to find out the average screen size of `smart phones`
```
db.electronics.aggregate([ { '$match': { 'type': 'smart phone' } },
                           { '$group': { '_id': 'smart phone',
                                         'average': { '$avg': '$screen size' } } }
] )
```  
<img width="750px" alt="image" src="images/2-7 mongo-query-mobiles2.png" />

### Task 8 - Export the fields `_id`, “type”, “model”, from the ‘electronics’ collection into a file named `electronics.csv`
<img width="750px" alt="image" src="images/2-8 mongoexport.png" />

