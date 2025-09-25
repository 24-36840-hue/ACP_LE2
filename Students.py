class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
    # 👉 initialize attributes here      
        self.id_name = (student_id, student_name)
        self.email = email
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else set()
    
    def __str__(self):
    # 👉 return formatted string of student info
        return (f"ID: {self.id_name[0]}, " 
                f"Name: {self.id_name[1]}, " 
                f"Email: {self.email}, "
                f"Grades: {self.grades if self.grades is not None else "No grades"}, "
                f"Courses: {self.courses if self.courses is not None else "No courses"}")
    
    def calculate_gpa(self):
    # 👉 convert scores into GPA scale (A=4.0, B=3.0, etc.)
    # 👉 compute and return average GPA
        if not self.grades:
            return None
        total = 0 
        count = 0 

        for score in self.grades.values(): 
            if isinstance(score, str): 
                grade = score.upper() 
                gpa = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}.get(grade, 0.0) 
            else:
                if score >= 90:
                    gpa = 4.0
                elif score >= 80:
                    gpa = 3.0
                elif score >= 70:
                    gpa = 2.0
                elif score >= 60:
                    gpa = 1.0
                else:
                    gpa = 0.0
            total += gpa 
            count += 1 
        return round(total / count, 2) if count else None 

class StudentRecords:
    def __init__(self):
    # 👉 initialize empty list for students
        self.students = []
        
    def add_student(self, student_id, student_name, email, grades=None, courses=None):
    # 👉 create Student object and append to list
        new_student = Student(student_id, student_name, email, grades, courses)
        self.students.append(new_student)
    # 👉 return "Student added successfully"
        return "Student added successfully"
    
    def update_student(self, student_id, email=None, grades=None, courses=None):
    # 👉 find student by ID
    # 👉 update only provided values
    # 👉 return success or not found
        for student in self.students:
            if student.id_name[0] == student_id:
                if email is not None:
                    student.email = email
                if grades is not None:
                    student.grades = grades
                if courses is not None:
                    student.courses = courses
                return "Student information updated successfully"
        return "Student not found"
    
    def delete_student(self, student_id):
    # 👉 remove student if found
    # 👉 return "Student deleted successfully" or "Student not found"
        for student in self.students:
            if student.id_name[0] == student_id:
                self.students.remove(student)
                return "Student deleted successfully"
        return "Student not found" 
    
    def enroll_course(self, student_id, course):
    # 👉 add course to student’s set (duplicates handled automatically)
    # 👉 return success or not found
        for student in self.students:
            if student.id_name[0] == student_id:
                student.courses.add(course)
                return "Course enrolled successfully"
        return "Student not found"
    
    def search_student(self, student_id):
    # 👉 return student info if found, else "Student not found"
        for student in self.students:
            if student.id_name[0] == student_id:
                return (student)
        return "Student not found"
    
    def search_by_name(self, name):
    # 👉 check if name.lower() is in student.id_name[1].lower()
    # 👉 return all matches
        self.name = name.lower()
        matches = [str(student) for student in self.students if name in student.id_name[1].lower()]
        return matches if matches else "No matching students found"

records = StudentRecords()
print("Student Records System")
print("----------------------")
# Add students (ID, Name, Email, Grades, Courses)
print(records.add_student(1001, "Mark", "mark@gmail.com", grades={"Math": "A", "Science": "B"}, courses={"Math", "Science"}))
print(records.add_student(1002, "Lucy", "lucy@gmail.com"))
print(records.enroll_course(1002, "History"))
print(records.update_student(1002, grades={"History": "A"}))
print(records.search_student(1001))
print(records.search_by_name("lucy"))
print(records.delete_student(1001))
print(records.search_student(1001))
print(records.search_by_name("mark"))
print("Lucy's GPA:", [student.calculate_gpa() for student in records.students if student.id_name[0] == 1002][0]) 
