class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Student:
    def __str__(self, some_lecturer):
        return '''
Имя: Ruoy
Фамилия: Eman
Средняя оценка за домашние задания: 9.9
Курсы в процессе изучения: Python, Git
Завершенные курсы: Введение в программирование'''
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
    def student_chart(self, grade):
        self.grade = grade
class Lecturer(Mentor):
    def __str__(self, some_lecturer):
        return '''
Имя: Some
Фамилия: Buddy
Средняя оценка за лекции: 9.9'''
    def __init__(self, grades):
        self.grades = {}
    def lecturer_chart(self, grade):
        self.grade = grade       
    
class Reviewer(Mentor):
    def __str__(self, some_reviewer):
        return '''
Имя: Some
Фамилия: Buddy'''
          
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'   
    
man1 = Student('Nill', 'Braun', 8)
man2 = Student('Rick', 'Soul', 10)
man3 = Reviewer('Bill', 9)
man4 = Reviewer('Jonn', 10)

 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)
