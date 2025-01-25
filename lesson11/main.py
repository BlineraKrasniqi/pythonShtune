import datetime
import datetime

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



