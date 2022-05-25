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


class CFGStudent:

    def __init__(self, name, surname, age, email, student_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = dict()
        
    @staticmethod
    def generate_id(student_id):
        if id not in student_id:
            student_id[id] = 1
        else:
            student_id[id] = student_id[id] + 1

    def get_id(self):
        print('Student_id: ', self.student_id)

    def get_fullname(self):
        print('Name: ', self.name, 'Surname: ', self.surname)

class NanoStudent(CFGStudent):

    def __init__(self, name, surname, age, email, student_id, specialization, course_grades):
        super().__init__(name, surname, age, email, student_id)
        self.specialization = specialization
        self.course_grades = course_grades

    @staticmethod
    def generate_id():
            def generate_id(student_id):
        if id not in student_id:
            student_id[id] = 1
        else:
            student_id[id] = student_id[id] + 1

    def add_new_grade(self, 'your code goes here'):
        'your code goes here'
        'update course_grades container'
        "Example: pass in a task name and its grade, so that both are added to course_grades"

    def get_course_grades(self):
        'your code goes here'
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
