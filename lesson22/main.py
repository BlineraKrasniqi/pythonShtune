from pydantic import BaseModel, coinit, constr
from typing import Optional

# class User(BaseModel):
#     id: int
#     name: str
#     age:int
#     email: str
#
# user = User(id=1, name ='John', age=18, email= 'john@exampe.compp')

class User(BaseModel):
    id: int
    name: str
    age Optional[int]:None
    email Optional[str]: None

user1 = User(id=1, name ='John', age=18, email= 'john@exampe.compp')
print(user1)

user2 = User(id=1, name ='John', email= 'john@exampe.compp')
print(user2)


user3 = User(id=1, name ='John')
print(user3)

class another_user(BaseModel):
    id: conint(gt=0)
    name: constr(min_length=2, max_length=50)

valid_user = another_user(id=1, name='John')
print(valid_user

valid_user1 = another_user(id=0, name='John')
print(valid_user1)



