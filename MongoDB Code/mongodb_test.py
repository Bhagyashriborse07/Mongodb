from pymongo import MongoClient

# Correct connection string
client = MongoClient("mongodb+srv://Bhagyashri:Bhagyashri%40123@bhagyashri.6fwpeqg.mongodb.net/mydatabase?retryWrites=true&w=majority")

db = client['mydatabase']  # database name
collection = db['mycollection']  # collection name

# Insert example document
collection.insert_one({"name": "Alice", "age": 25})

# Print all documents
for doc in collection.find():
    print(doc)

    
