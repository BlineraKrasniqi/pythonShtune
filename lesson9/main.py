# class Animal:
#     def sound(self):
#         print("A animal noise")
#
# class Dog(Animal):
#     def sound(self):
#         print("Woof Woof!!")
#
#
# class Cat(Animal):
#     def sound(self):
#         print("Meow Meow!!")
#
#
#
# animal = Animal()
# animal.sound()
#
# dog = Dog()
# dog.sound()
#
#
# cat = Cat()
# cat.sound()


# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def display_info(self):
#         print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
#
# class Car(Vehicle):
#     def __init__(self, make,model,year,body_style):
#         super(). __init__(make,model,year,body_style)
#         self.body_style = body_style
#
#
# class ElectricCar(Car):
#     def __init__(self, make,model,year,body_style, battery_capacity):
#         super(). __init__(make,model,year,body_style, battery_capacity)
#         self.battery_capacity = battery_capacity
#
#         def charge(self):
#             print("Charging the battery of electric car!!")
#
# tesla = ElectricCar("Tesla","CyberTruck","2024","SQUARE", "600km")
# tesla.display_info()
# print("Body style:", tesla.body_style)
# print("battery capacity:", tesla.battery_capacity)
# tesla.charge()


string_length = len ("Hello World")
list_length = len ([1,2,3,4,5,6,7,8])
tuple_length = len ([10.20,30])


print(string_length)
print(list_length)
print(tuple_length)
