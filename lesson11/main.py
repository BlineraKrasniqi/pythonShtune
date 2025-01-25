import datetime
import datetime
import os.path

currentdatetime = datetime.datetime.now()

print("Year:" ,currentdatetime.year)
print("Month:", currentdatetime.month)
print("Hour:" ,currentdatetime.hour )
print("Second:" , currentdatetime.year)


currentdate = datetime.datetime.now().date()

currentdate = datetime.datetime.now().date()


print(currentdate)

settime = datetime.datetime.now().time()

specefictime = datetime.date (2024, 3 , 2)

print(specefictime)

plusdays =  currentdate + datetime.timedelta(days=100)
print(plusdays)

minusdays =  currentdate - datetime.timedelta(days=100)
print(minusdays)


with open("example.txt", "w") as file:
    print("Hello world")

file_path = "example.txt"
file = open(file_path, "r")

content = file.read()
print(content)
file.close()

with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)

with open ("example.txt", "r") as file:
    line = file.readline()
    print(line)


if os.path.exists("example.txt"):
    print("file exists!")


