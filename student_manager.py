from student import Student
import json
import os

class StudentManager:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    data = json.load(f)
                    self.students = [Student.from_dict(item) for item in data]
                except json.JSONDecodeError:
                    self.students = []

    def save_students(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([student.to_dict() for student in self.students], f, indent=4)

        with open('std_data.txt', 'w', encoding='utf-8') as  txt_file:
            for student in self.students:
                txt_file.write(str(student.to_dict()) + '\n')


    def add_student(self, student):
        self.students.append(student)
        self.save_students()

    def view_student(self):
      if not self.students:
        return ['No students found.']
      return self.students



    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def update_student(self, student_id, name=None, age=None, grade=None):
        student = self.find_student(student_id)
        if student:
            if name:
                student.name = name
            if age is not None:
                student.age = age
            if grade:
                student.grade = grade
            self.save_students()
            return True
        return False

    def delete_students(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            self.save_students()
            return True
        return False