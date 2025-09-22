from pymongo import MongoClient

# Connect to MongoDB (replace connection string if using Atlas)
client = MongoClient("")

# Access the database (it will be created if it doesn't exist)
db = client["mydatabase"]

# Access a collection (like a table)
collection = db["users"]

# 1. Insert a document
user = {"name": "Bhagyashri", "age": 25, "email": "bhagyashri@example.com"}
result = collection.insert_one(user)
print("Inserted ID:", result.inserted_id)

# 2. Find a document
found_user = collection.find_one({"name": "Bhagyashri"})
print("Found User:", found_user)

# 3. Update a document
collection.update_one({"name": "Bhagyashri"}, {"$set": {"age": 26}})
print("User age updated")

# 4. Delete a document
collection.delete_one({"name": "Bhagyashri"})
print("User deleted")

