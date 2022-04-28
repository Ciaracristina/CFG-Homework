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

    def add_subject_and_mark(self, subject, mark):
        self.subjects[subject] = mark

    def remove_subject_and_mark(self, subject):
        del self.subjects[subject]

    def all_subjects_taken(self, name, subjects):
        self.name()
        self.subjects[subjects]



class CFGStudent(Student):

    def __init__(self, name, age, id, specialisation):
        super().__init__(name, age, id)
        self.specialisation = specialisation


ciara = CFGStudent('Ciara', 30, 1, 'software')
benji = CFGStudent('Benji', 31, 2, 'history')


ciara.add_subject_and_mark('art', 80)
ciara.add_subject_and_mark('fullstack', 80)
ciara.add_subject_and_mark('fullstack', 80)
print(ciara.subjects)
ciara.remove_subject_and_mark('fullstack')
print(ciara.subjects)
print(ciara.all_subjects_taken())



#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

class Vehicle:

    def __init__(self, number_of_wheels, engine_size):
        self.number_of_wheels = number_of_wheels
        self.engine_size = engine_size


class Car(Vehicle):

    def __init__(self, make, model, year, engine_size):
        super().__init__(4, engine_size)
        self.make = make
        self.model = model
        self.year = year

mini = Car('mini', 'cooper', 2000, 2)


class Bike(Vehicle):

    def __init__(self, colour, style):
        super().__init__(2, None)
        self.colour = colour
        self.style = style

racing = Bike('black', 'racing')