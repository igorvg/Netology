from itertools import chain
import numpy

class Student:
    all_students = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = ()
        self.all_students.append(self)


    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses) \
                and course in lecturer.courses_attached and grade in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]

            else:
                lecturer.grades[course] = [grade]

        else:
            print('Ошибка')

    def average(self):
        self.average_grade = round(numpy.average(list(chain(*self.grades.values()))), 2) if len(list(chain(*self.grades.values()))) !=0 else 0


    def __str__(self):
        self.average()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершённые курсы: {", ".join(self.finished_courses) if len(self.finished_courses) !=0 else "Отсутствуют"}'
        return res

    def __lt__(self, other):
        self.average()
        other.average()
        if not isinstance(other, Student):
            print('Так не пойдёт.')
            return
        return self.average_grade < other.average_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    all_lecturers = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = 0
        self.all_lecturers.append(self)


    def rate(self, student, course, grade):
        print('Лекторы не могут ставить оценки.')

    def average(self):
        Student.average(self)

    def __str__(self):
        self.average()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}'
        return res

    def __lt__(self, other):
        self.average()
        other.average()
        if not isinstance(other, Lecturer):
            print('Так не пойдёт.')
            return
        return self.average_grade < other.average_grade

class Reviewer(Mentor):

    def rate(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

        else:
            print('Ошибка')

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res



mike = Student('Mike', 'Wazovsky', 'male')
sally = Student('James', 'Sallyvan', 'male')

rose = Reviewer('Rose ', 'Slither')
henry = Reviewer('Henry', 'Waternoose')

abigail = Lecturer('Abigail', 'Hardscrabble')
alfred = Lecturer('Alfred', 'Knight')

mike.courses_in_progress = ['Canister Design', 'Door Design', 'Scaring', 'Computer Sciences']
sally.courses_in_progress = ['Computer Sciences', 'Acting', 'Directing']
mike.finished_courses = ['Computer Sciences']

abigail.courses_attached = ['Computer Sciences', 'Scaring', 'Canister Design']
alfred.courses_attached = ['Door Design', 'Directing', 'Canister Design']
rose.courses_attached = ['Acting', 'Canister Design', 'Directing']
henry.courses_attached = ['Computer Sciences', 'Scaring', 'Canister Design']

rose.rate(mike, 'Canister Design', 6)
henry.rate(mike, 'Scaring', 2)
henry.rate(mike, 'Canister Design', 1)
henry.rate(mike, 'Computer Sciences', 4)

rose.rate(sally, 'Acting', 2)
rose.rate(sally, 'Directing', 3)
henry.rate(sally, 'Computer Sciences', 2)
henry.rate(sally, 'Computer Sciences', 10)

sally.rate(abigail, 'Computer Sciences', 10)
mike.rate(abigail, 'Scaring', 7)
mike.rate(alfred, 'Canister Design', 2)
mike.rate(alfred, 'Door Design', 9)
sally.rate(alfred, 'Directing', 5)

def what_about_students(students, course):
    another_average = []
    for i in students:
        if course in i.grades:
            another_average += i.grades[course]
    print(f'Средний балл у студентов по курсу {course}: {round(numpy.average(another_average), 2)}')


def what_about_lecturers(lecturers, course):
    another_average = []
    for i in lecturers:
        if course in i.grades:
            another_average += i.grades[course]

    print(f'Средняя оценка за лекции по курсу {course}: {round(numpy.average(another_average), 2)}')



print(sally)