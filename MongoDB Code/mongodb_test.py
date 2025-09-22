from pymongo import MongoClient

# Correct connection string
client = MongoClient("")

db = client['mydatabase']  # database name
collection = db['mycollection']  # collection name

# Insert example document
collection.insert_one({"name": "Alice", "age": 25})

# Print all documents
for doc in collection.find():
    print(doc)

    

