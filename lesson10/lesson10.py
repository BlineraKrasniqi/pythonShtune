# from abc import ABC, abstractmethod
# # class Student:
# #     def __init__(self, name, age):
# #         self.__name = name
# #         self.__age = age
# #
# #     def get_name(self):
# #         return self.__name
# #
# #
# #     def set_name(self, name):
# #       self.__name = name
# #
# #     def get_age(self):
# #         return self.__age
# #
# #     def set_age(self, age):
# #         self.__age = age
# #
# #
# # student1 = Student("Liron", 16)
# # print("Name:", student1.get_name())
# # student1.set_name("LironA")
# # print("Updated name:", student1.get_name())
# #
# # print("age", student1.get_age())
# # student1.set_age(17)
# # print("Updated age:", student1.get_age())
from abc import abstractmethod


class Printalble(ABC):

    @abstractmethod
    def print_info(self):
        pass

    class Book(Printable):
        def __init__(self, title, author):
            self.title = title
            self.author = author

        def print_info(self):
            print(f"Book: {self.title} by {self.author}")

book = Book ("fuqia e se tashmes", "Ismail Kadare")

book.print_info()






#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __int__(self,radius):
#      self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
#
# class Square(Shape):
#     def __init__(self,length):
#         self.length = length
#
#         def area(self):
#             return self.length * self.length
#
#
#
# circle_1 = Circle(17)
# square_1 = Square(10)
#
# print(circle_1.area())
# print(square_1.area())
