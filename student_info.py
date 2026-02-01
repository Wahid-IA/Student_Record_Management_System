class Student_info():

    #Initiating Student details
    def __init__(self, name, roll, email, dep):
        self.student_name= name
        self.student_roll= roll
        self.student_email= email
        self.student_department= dep

    #Converting the Class object to dictionary to store as json file
    def to_dict(self):
        return{
            "Name": self.student_name,
            "Roll": self.student_roll,
            "Email": self.student_email,
            "Department": self.student_department
        }
    
    #Converting the dictionary back to Class object for loading data from json file
    @staticmethod
    def from_dict(data):
        return Student_info(
            data["Name"],
            data["Roll"],
            data["Email"],
            data["Department"]
        )