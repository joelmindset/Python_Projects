#parent class
class Person:
    name = "Unknown"
    age = 0
    study = "Unknown"
    studentId = 0
    Teacher = True
    wage = None
    dateOfHire = "unknown"
    department = "Unknown"
#child class
class Student(Person):
    name = "Bob"
    studentId = 46789
    study = "Math"
    age = 28
    Teacher = False

    #return info for name, id, study
    def stundentInfo(self):
        msg = "\nName: {}\nID: {}\nStudy: {}".format(self.name,self.studentId,self.study)
        return msg
#child class
class Teacher(Person):
    name = "Steve"
    age = 48
    Teacher = True
    wage = 40
    dateOfHire = "03/16/95"
    department = "English"
    #return info for name dateOfHire department
    def teacherInfo(self):
        msg = "\nName: {}\nDate of hire: {}\nDepartment: {}".format(self.name,self.dateOfHire,self.department)
        return msg

#call stundent and teacher and print info
if __name__ == "__main__":
    teacher = Teacher()
    student = Student()
    print(teacher.teacherInfo())
    print(student.stundentInfo())