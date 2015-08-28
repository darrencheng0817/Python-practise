#appointment with prof
class Person():

    def __init__(self, name, age, SIN, phone):
        self._name = name
        self._age = age
        self._SIN = SIN
        self._phone = phone

    def __str__(self):
        return "Hi, I'm " + self._name

    def set_eye_colour(self, colour):
        self._eye_colour = colour

    def get_eye_colour(self):
        return self._eye_colour


class Student(Person):

    def __init__(self, name, age, SIN, phone, GPA, student_num):
        Person.__init__(self, name, age, SIN, phone)
        self._GPA = GPA
        self._student_num = student_num

    def __str__(self):
        return Person.__str__(self) + \
            "and my student number is " + self._student_num


class Faculty(Person):

    def __init__(self, name, age, SIN, phone, office):
        Person.__init__(self, name, age, SIN, phone)
        self._office = office

    def __str__(self):
        return Person.__str__(self) + " and my office is: " + self._office
