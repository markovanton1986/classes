class Student:
    def __init__(self, name, surname, gender):
        self.name  =name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_inprogress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
 (course in self.courses_inprogress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grades(self):
        if not self.grades:
            return 'Нет оценок'
        else:
            all_grades = sum(self.grades.values(), [])
            return sum(all_grades) / len(all_grades)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n' \
              f'Средняя оценка за домашнее задание: {self._average_grades()} \n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_inprogress)} \n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self._average_grades() < other._average_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grades(self):
        if not self.grades:
            return 'Нет оценок'
        else:
            all_grades = sum(self.grades.values(), [])
            return sum(all_grades) / len(all_grades)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._average_grades()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self._average_grades() < other._average_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course  in self.courses_attached and \
 (course in student.courses_inprogress or course in student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


def aver_gr_st(students, course):
    all_grades = []
    for student in students:
        all_grades += student.grades.get(course)
    aver = sum(all_grades)/len(all_grades)
    return aver


def aver_gr_lec(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        all_grades += lecturer.grades.get(course)
    aver = sum(all_grades) / len(all_grades)
    return aver


student1 = Student('Anton', 'Markov', 'm')
student1.courses_inprogress += ['Java', 'SQL', 'Git']
student2 = Student('Alex', 'Smith', 'm')
student2.courses_inprogress += ['Python', 'C++', 'Java']


lecturer1 = Lecturer('Thomas', 'Wilson')
lecturer2 = Lecturer('Fred', 'Evans')
lecturer1.courses_attached += ['Python', 'Java', 'C++']
lecturer2.courses_attached += ['C++', 'Git', 'SQL']

reviewer1 = Reviewer('David', 'Jones')
reviewer2 = Reviewer('Tyler', 'Moore')
reviewer1.courses_attached += ['Java', 'Git', 'SQL']
reviewer2.courses_attached += ['Python', 'C++', 'SQL']

student1.add_courses('Python')
student2.add_courses('Java')
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Java', 9)
student1.rate_lecturer(lecturer2, 'SQL', 8)
student1.rate_lecturer(lecturer2, 'Git', 9)
student2.rate_lecturer(lecturer1, 'Java', 9)
student2.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer2, 'SQL', 9)
student2.rate_lecturer(lecturer2, 'C++', 7)
student2.rate_lecturer(lecturer1, 'C++', 8)

reviewer1.rate_hw(student1, 'Java', 9)
reviewer1.rate_hw(student1, 'Git', 9)
reviewer2.rate_hw(student1, 'SQL', 10)
reviewer1.rate_hw(student2, 'SQL', 8)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Java', 7)

print(student1)
print(student2)
print(lecturer2)
print(lecturer1)
print(reviewer2)
print(student1 < student2)
print(lecturer2 > lecturer1)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print(aver_gr_lec(lecturers, 'C++'))
print(aver_gr_st(students, 'Python'))