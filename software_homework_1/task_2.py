"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()
        self.avg_mark = None

    def add_subject_and_mark(self, subject, mark):
        self.subjects[subject] = mark

    def remove_subject_and_mark(self, subject):
        del self.subjects[subject]

    # returns a list of all subjects for student
    def all_subjects_taken(self, subject):
        return self.subjects.keys()

    # returns students average mark. aka sum all marks and divide by number of marks
    def average_mark(self):
        all_marks = self.subjects.values()
        running_total = 0

        for mark in all_marks:
            running_total += mark

        self.avg_mark = running_total
        return self.avg_mark


class CFGStudent(Student):

    def __init__(self, name, age, id, specialisation):
        super().__init__(name, age, id)
        self.specialisation = specialisation


ciara = CFGStudent('Ciara', 30, 1, 'software')
benji = CFGStudent('Benji', 31, 2, 'history')


ciara.add_subject_and_mark('art', 70)
ciara.add_subject_and_mark('fullstack', 80)
ciara.add_subject_and_mark('music', 55)
ciara.add_subject_and_mark('maths', 73)
print(ciara.subjects)
ciara.remove_subject_and_mark('fullstack')
print(ciara.subjects)




#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

