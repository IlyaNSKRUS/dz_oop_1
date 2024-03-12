class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _Average(self):
        gradelist = sum(list(self.grades.values()), [])
        return round(sum(gradelist) / len(gradelist), 1)

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self._Average()}'

    def __lt__(self,other):
        return self._Average() < other._Average()
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def _Average(self):
        gradelist = sum(list(self.grades.values()), [])
        return round(sum(gradelist) / len(gradelist), 1)

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._Average()}'

    def __lt__(self,other):
        return self._Average() < other._Average()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}'

student1 = Student('Ivan', 'Ivanov', 'Man')
student2 = Student('Petr', 'Petrov', 'Man')
student3 = Student('Elena', 'Stepanova', 'Woman')
student1.courses_in_progress += ['Python', 'Git']
student2.courses_in_progress += ['Python', 'Git']
student3.courses_in_progress += ['Python', 'Git']

lecturer1 = Lecturer('Oleg', 'Smirnov')
lecturer2 = Lecturer('Anna', 'Sergeeva')
lecturer3 = Lecturer('Igor', 'Akinfeev')
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']
lecturer3.courses_attached += ['Git']

reviewer1 = Reviewer('Roman', 'Zobnin')
reviewer2 = Reviewer('Aleksandr', 'Sobolev')
reviewer3 = Reviewer('Evgeny', 'Baranov')
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Python']
reviewer3.courses_attached += ['Git']
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student3, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student1, 'Python', 6)
reviewer2.rate_hw(student3, 'Python', 9)
reviewer3.rate_hw(student1, 'Git', 10)
reviewer3.rate_hw(student2, 'Git', 10)
reviewer3.rate_hw(student3, 'Git', 10)
reviewer3.rate_hw(student1, 'Git', 9)
reviewer3.rate_hw(student2, 'Git', 5)
reviewer3.rate_hw(student3, 'Git', 8)

student1.rate_hw(lecturer1, 'Python', 10)
student1.rate_hw(lecturer2, 'Python', 9)
student1.rate_hw(lecturer3, 'Git', 9)
student2.rate_hw(lecturer2, 'Python', 8)
student2.rate_hw(lecturer1, 'Python', 6)
student2.rate_hw(lecturer3, 'Git', 6)
student3.rate_hw(lecturer1, 'Python', 6)
student3.rate_hw(lecturer2, 'Python', 6)
student3.rate_hw(lecturer3, 'Git', 6)

print(f'Проверяющий:',reviewer1)
print(f'Лектор:',lecturer1)
print(f'Студент:',student1)
print(f'\nСредняя оценка студента 1 за ДЗ больше средней оценки студента 2 :', student2 < student1)
print(f'\nСредняя оценка лектора 1 за лекции больше средней оценки лектора 2 :', lecturer2 < lecturer1)

student_list = []
student_list.append(student1)
student_list.append(student2)
student_list.append(student3)
lecturer_list = []
lecturer_list.append(lecturer1)
lecturer_list.append(lecturer2)
lecturer_list.append(lecturer3)
def average_dz(lst, course):
    pages_course_stud = []
    for item in lst:
        pages_course_stud.extend(item.grades[course])
        average_course = round(sum(pages_course_stud) / len(pages_course_stud),1)
    print(f'\nСреднее оценка за ДЗ на курсе {course}:',average_course)
average_dz(student_list,'Python')
def average_lec(lst, course):
    pages_lec = []
    for item in lst:
        if course in item.grades:
            pages_lec.extend(item.grades[course])
        else:
            pass

    average_lec = sum(pages_lec) / len(pages_lec)
    print(f'\nСреднее оценка лекторов на курсе {course}:',average_lec)
average_lec(lecturer_list, 'Python')