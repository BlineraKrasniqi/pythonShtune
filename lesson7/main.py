from lesson7 import result

try:
    result =10/1

except ZeroDivisionError:
    print("Division by zero has accoured")

else:
 print("Division by zero error has accured", result)

 try:
     result= 10/2
 except ZeroDivisionError:
     print("Can not be divided")

finally:
    print("Finally the block is executed")











