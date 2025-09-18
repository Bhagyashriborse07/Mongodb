from pymongo import MongoClient

# Connection string (replace with your own credentials)
connection_string ="mongodb+srv://Bhagyashri:Bhagyashri%40123@bhagyashri.6fwpeqg.mongodb.net/mydatabase?retryWrites=true&w=majority"

# Create a client and connect to MongoDB
client = MongoClient(connection_string)
db = client['mydatabase1']
collection = db['users']  # Collection name

# Function to insert a document
def insert_user(name, age, city):
    user = {
        "name": name,
        "age": age,
        "city": city
    }
    result = collection.insert_one(user)
    print("User inserted with ID:", result.inserted_id)

# Function to find users
def find_users():
    users = collection.find()
    for user in users:
        print(user)

# Function to update a user's age
def update_user(name, new_age):
    result = collection.update_one(
        {"name": name},
        {"$set": {"age": new_age}}
    )
    print(f"Matched: {result.matched_count}, Updated: {result.modified_count}")

# Function to delete a user
def delete_user(name):
    result = collection.delete_one({"name": name})
    print(f"Deleted {result.deleted_count} user(s) with name {name}")

# Main execution
if __name__ == "__main__":
    print("Connecting to MongoDB...")

    # Insert users
    insert_user("Alice", 25, "Pune")
    insert_user("Bob", 30, "Mumbai")

    # Find and display all users
    print("\nAll users:")
    find_users()

    # Update Alice's age
    update_user("Alice", 26)

    # Find and display all users again
    print("\nUsers after update:")
    find_users()

    # Delete Bob's record
    delete_user("Bob")

    # Final list of users
    print("\nUsers after deletion:")
    find_users()
