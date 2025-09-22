from pymongo import MongoClient

# MongoDB Atlas connection string
client = MongoClient("")

# Access the database and collection
db = client["todoapp"]
tasks = db["tasks"]

# Insert a new task

task = {"title": "Learn Python", "description": "Complete Python basics", "completed": False}
result = tasks.insert_one(task)
print("Task inserted with ID:", result.inserted_id)

# Get and display all tasks
print("All tasks:")
for task in tasks.find():
    print(task)

