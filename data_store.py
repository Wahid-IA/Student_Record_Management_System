import json
from student_info import Student_info

#JSON file
file_name= "stored_students.json"

#Storing Student records into JSON file
def save_students(student_list):
    with open(file_name, "w") as f:
        json.dump([s.to_dict() for s in student_list],f, indent=4)

#Loading Student records from JSON file
def load_students():
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
            return [Student_info.from_dict(d) for d in data]
    except FileNotFoundError:
        return []

#Loading Student records from JSON file at startup
#Keeping in a variable to modify 
created_s= load_students()