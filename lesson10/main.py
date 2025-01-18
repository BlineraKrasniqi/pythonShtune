from tkinter.font import names


class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name


    def set_name(self, name):
      self.__name = name

    def get_age(self):
        return self.__age

    def get_age(self, age):
        self.__age = age


studenti1 = Student("Liron", 16)
print("Name:", studenti1.get_name())
studenti1.set_name("LironA")
print("Updated name:", studenti1.get_name())

print("Age", studenti1.get_age())
studenti1.set_age(17)
print("Updated age:", studenti1.get_age())