from pymongo import MongoClient

# -----------------------------
# Step 1: Connect to MongoDB
# -----------------------------
client = MongoClient(
    "mongodb+srv://Bhagyashri:Bhagyashri%40123@bhagyashri.6fwpeqg.mongodb.net/mydatabase?retryWrites=true&w=majority"
)

# Access the database
db = client['mydatabase']

# Access the collection
collection = db['mycollection']

# -----------------------------
# Step 2: CREATE
# -----------------------------
# Insert one document
collection.insert_one({"name": "Alice", "age": 25, "city": "Mumbai"})

# Insert multiple documents
collection.insert_many([
    {"name": "Bob", "age": 30, "city": "Delhi"},
    {"name": "Charlie", "age": 28, "city": "Pune"},
    {"name": "David", "age": 35, "city": "Bangalore"}
])

print("Documents inserted successfully!")

# -----------------------------
# Step 3: READ
# -----------------------------
print("\n--- All Documents ---")
for doc in collection.find():
    print(doc)

print("\n--- Documents where age > 28 ---")
for doc in collection.find({"age": {"$gt": 28}}):
    print(doc)

# -----------------------------
# Step 4: UPDATE
# -----------------------------
# Update one document
collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})

# Update multiple documents
collection.update_many({"city": "Delhi"}, {"$set": {"city": "New Delhi"}})

print("\nDocuments updated successfully!")

# Verify updates
print("\n--- Documents after update ---")
for doc in collection.find():
    print(doc)

# -----------------------------
# Step 5: DELETE
# -----------------------------
# Delete one document
collection.delete_one({"name": "Charlie"})

# Delete many documents where age < 30
collection.delete_many({"age": {"$lt": 30}})

print("\nDocuments deleted successfully!")

# Verify deletion
print("\n--- Documents after deletion ---")
for doc in collection.find():
    print(doc)

# -----------------------------
# Step 6: COUNT & SORT
# -----------------------------
total_docs = collection.count_documents({})
print("\nTotal documents in collection:", total_docs)

print("\n--- Documents sorted by age descending ---")
for doc in collection.find().sort("age", -1):
    print(doc)
