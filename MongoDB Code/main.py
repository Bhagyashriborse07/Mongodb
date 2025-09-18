from pymongo import MongoClient


if __name__ == '__main__' :
    client = MongoClient("mongodb+srv://Bhagyashri:Bhagyashri%40123@bhagyashri.6fwpeqg.mongodb.net/mydatabase?retryWrites=true&w=majority")

    db = client['wisdom-academy']

    collection = db.class1

    studentInfo = {
        "name" : "Rinku",
        "section" : 1,
        "math_marks" : 85,
        "ssc_marks" :90
    }
student_id = collection.insert_one(studentInfo) . inserted_id
print(f"Student with id {student_id}  has been created")