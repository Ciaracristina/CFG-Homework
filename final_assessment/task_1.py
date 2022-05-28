# TASK 1
#
# Design a parent class called CFGStudent.
#
# It should have general attributes like name, surname, age, email, student id
# and methods to fetch student’s full name and student’s id.
#
# Design a child class called NanoStudent, which  inherits from CFGStudent class.
# This class should have exactly the same attributes as its parent class,
# as well as an additional one called ‘specialization’ and course grades.
#
# The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
# in front of the id.
#
# New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
# You can use  it as a skeleton code for your classes OR adjust it and create your own.
#
# SEE NOTES BELOW
import random
import uuid

class CFGStudent:

    def __init__(self, name, surname, age, email, student_id=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = self.generate_id(student_id)

    def generate_id(self, student_id):
        if student_id is None:
            return str(uuid.uuid1())
        else:
            return student_id


    def get_id(self):
        return self.student_id

    def get_fullname(self):
        return '{first_name} {surname}'.format(first_name=self.name, surname=self.surname)


class NanoStudent(CFGStudent):

    def __init__(self, name, surname, age, email, specialization, course_grades, student_id=None):
        super().__init__(name, surname, age, email, student_id)
        self.specialization = specialization
        self.course_grades = dict()

    def generate_id(self):
        return 'NANO-{id}'.format(id=super().get_id())

    def add_new_grade(self, course, grade):
        self.course_grades[course] = grade
        'update course_grades container'
        "Example: pass in a task name and its grade, so that both are added to course_grades"

    def get_course_grades(self):
        return self.course_grades
        'fetch course grades container and its values'

############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}
