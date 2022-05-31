"""
TASK 1

(A)
Design a parent class called Animal

It must have general attributes: name, date of birth, colour, owner's name
Also it must have a method that gives you the age of an animal.

For example, if animal's date of birth is 2021/08/21 and today is
11 January 2021, the when you call get_age()
<name your method whatever you want> method, it should give us the age in
YEAR and MONTH like this: {'years': 0, 'months': 4}

(B)
B.1
Design a child class called Dog, which inherits from the Animal class.
This class should have exactly the same attributes as its parent class,
as well as additional ones called:
pet_id and breed (any other attributes are welcome - they are optional).
You child class Dog should also have a static method called sound(), which
would give us the sound of the animal ('Grr', 'Bark', whatever you want)

B.2
Design a child class called Cat, which inherits from the Animal class.
This class should have exactly the same attributes as its parent class,
as well as additional ones called:
pet_id and breed (any other attributes are welcome - they are optional).
You child class Dog should also have a static method called sound(), which
would give us the sound of the animal ('Meow', 'Purr', whatever you want)

(C)
Design an independent class called PetOwner. It is a small class, which should
have the __init__ method only accepting the 'name of an owner' and 'pet's id'.

SEE THE STARTER CODE BELOW

"""
from datetime import date


class Animal:

    def __init__(self, name, dob, colour, owner):
        self.name = name
        self.dob = dob
        self.colour = colour
        self.owner = owner

    def get_age(self, birthday, year, month):
        self.birthday = birthday
        today = date.today()
        age = today.year - birthday.year - ((today.month, today.day) < birthday.month, birthday.day)
        # you may need to import some packages to manipulate dates
        # <your code goes here>
        return {'years': int(year), 'months': int(month)}


class Dog(Animal):
    def __init__(self, name, dob, pet_id, breed):
        super().__init__(name, dob, colour, owner)
        self.pet_id = pet_id
        self.breed = breed

    def sound(self):
        print('WOOF')


class Cat(Animal):
    def __init__(self, name, dob, pet_id, breed):
        super().__init__(name, dob, colour, owner)
        self.pet_id = pet_id
        self.breed = breed
        self.sound = ()

    def sound(self):
        print('Meow')


class PetOwner:
    def __init__(self, name, pet_id):
        self.name = name
        self.pet_id = pet_id


print(Animal.get_age({'1991/5/28'}))

# <class Dog with additional attributes: pet_id and breed, sound method HERE>

# <class Cat with additional attributes: pet_id and breed, sound method HERE>

# <independent class PetOwner with name and pet_id attributes HERE>


"""
TASK 2

We are going to utilize classes that we created as part of TASK 1. 

Let's imagine that we are a local vet clinic and given the input below, we 
need to add all pets to our register (register is just a dict). 

Please write a function, which parses given input and initializes a class for
each animal, as well as its owner and adds it to the register by id. 

EXAMPLE OUTPUT:

{
 10025: <__main__.Dog object at 0x0829DFB8>,
 10026: <__main__.Cat object at 0x082B4D90>,
 10042: <__main__.Dog object at 0x082B4130>,
 10053: <__main__.Dog object at 0x082B47F0>,
 10058: <__main__.Cat object at 0x07C80B50>
 }

 Each key is a pet id and each value is a newly initialized  Dog or Cat class. 
 Note that within each Dog and Cat class the variable "self.owner" is also 
 a class PetOwner with all relevant attributes.

SEE THE STARTER CODE BELOW

"""
# this is the input for your function

pet_info = [
    {'breed': 'German Shepherd',
     'colour': 'brown',
     'dob': '2021/09/21',
     'pet_id': 10025,
     'name': 'Lola',
     'owner': 'Maria Smith',
     'type': 'dog'},
    {'breed': 'Blue Russian',
     'colour': 'white',
     'dob': '2010/03/06',
     'pet_id': 10058,
     'name': 'Snowy',
     'owner': 'Malcolm Graham',
     'type': 'cat'},
    {'breed': 'Border Collie',
     'colour': 'beige',
     'dob': '2019/11/18',
     'pet_id': 10042,
     'name': 'Bailey',
     'owner': 'Priya Patel',
     'type': 'dog'},
    {'breed': 'Pug',
     'colour': 'black',
     'dob': '2021/10/16',
     'pet_id': 10053,
     'name': 'Ziggy',
     'owner': 'Mohamed Moussa',
     'type': 'dog'},
    {'breed': 'Sphynx',
     'colour': 'white',
     'dob': '2015/08/23',
     'pet_id': 10026,
     'name': 'Coco',
     'owner': 'Jennifer Coley',
     'type': 'cat'}
]


class PetsInfo(Animal, PetOwner):
    def __init__(self, :

    def register_pets(self, pet_info):
        self.

        pets = dict()

        def pets(self, subject, mark):
            self.subjects[subject] = mark

        # <your code goes HERE>
        # don't forget to:
        # initialize the pet Owner as a class and reassign it to its Key
        # check the type to know which class to use for initialization
        # add a newly created pet (Cat or Dog) to your register by its id

        return pets

    print(register_pets(pet_info))

    """
    TASK 3
    
    Write a function to sum up the digits of a given number.
    
    EXAMPLE:
    
    num = 78
    result = 15
    
    num = 333
    result = 9
    
    num = 12345
    result = 15
    ===============================
    
    Using recursion = 25 points
    Any non recursive solution = 15 points
    
    ===============================
    
    Hints for recursive approach:
    
    1) Get the rightmost digit of the number with help of remainder 
    ‘%’ operator by dividing it with 10
    
    2) Dividing a number by 10 with help of ‘/’ operator and converting it to int
    helps you to 'move or iterate' through a number
    """

    def sum_of_given_number(input):
        str_input = str(input)
        if len(str_input) == 1:
            return input
        return int(str_input[0]) + sum_of_given_number(int(str_input[1:]))

    print(sum_of_given_number(78))
    print(sum_of_given_number(333))
    print(sum_of_given_number(12345))

    """
    TASK 4
    
    NON-CODING ASSIGNMENT
    
    *You need to write your answer as a mini essay.* 
    
    Please see the code example below. In this example, one of the SOLID 
    principles is violated. 
    
    1) Which SOLID principle is violated?
    2) How does this principle work and what is its fundamental meaning?
    3) Describe what is happening below and how a user who is running the TEST
     code can be confused?
    
    """

    class Rectangle:

        def __init__(self):
            self.width = None
            self.height = None

        def set_width(self, width):
            self.width = width

        def set_height(self, height):
            self.height = height

        def get_width(self):
            return self.width

        def get_height(self):
            return self.height

        def get_area(self):
            return self.width * self.height

    class Square(Rectangle):

        def set_width(self, width):
            self.width = width
            self.height = width

        def set_height(self, height):
            self.height = height
            self.width = height

    # TEST  - code run

    my_rectangle = Square()

    my_rectangle.set_height(5)
    my_rectangle.set_width(10)

    print(my_rectangle.get_area())

    # Dependency injection is the SOLID principle violated in this case as both classes, parent and child, are supposed to rely equally on one another to function whereas in this case the square function is creating its own setters and therefore not dependent on the parent class.
    # This principle usually allows you to control the key dependencies of an object and makes it clear what data and dependencies are needed for the function to run correctly. This can also be useful when you are testing as you can wire up different dependencies.
    # A user running this test could be confused as the square() class is called but named 'my_rectangle' and the measurements set would suggest that a rectangle is being returned due to the height and width being set differently.
    # This however is not the case as my_rectangle.set_width(10) was the last measurement to be set before printing the area of 'my_rectangle' in the set_width function of the Square class both the width and height are set to equal the width.
