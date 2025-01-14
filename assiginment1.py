class Student:
    def __init__(self, Name, RollNumber, Course, Age):
        self.Name = Name
        self.RollNumber = RollNumber
        self.Course = Course
        self.Age = Age
        
Student1 = Student("Ayushi", 101, "Data Science", 26)
Student2 = Student("Khushi", 102, "DevOps", 25)
Student3 = Student("Umang", 103, "AI/ML", 20)

print("\nStudent :",Student1.Name, "\nRollNumber :", Student2.RollNumber, "\nCourse :", Student1.Course, "\nAge :", Student1.Age)
print("\nStudent :",Student2.Name, "\nRollNumber :", Student2.RollNumber, "\nCourse :", Student2.Course, "\nAge :", Student2.Age)
print("\nStudent :",Student3.Name, "\nRollNumber :", Student3.RollNumber, "\nCourse :", Student3.Course, "\nAge :", Student3.Age)

        