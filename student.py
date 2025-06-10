class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f'ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}'

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade
        }

    @staticmethod
    def from_dict(data):
        return Student(data['student_id'], data['name'], data['age'], data['grade'])