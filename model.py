from pydantic import BaseModel, FieldSerilizationInfo,field_validator, conint, constr

class User(BaseModel):
    id: int
    name: str
    age: int

    @field_validator('age')
    def age_must_be_positive(cls, v, info:FieldSerilizationInfo):
        if v <= 0:
            raise ValueError('Age must be positive')
        return v

try:
    user = User(id=1, name="John", age= -1)
    print(user)

except ValueError as e:
    print(e)

class Adress(BaseModel):
    street: str
    city: str

class Users(BaseModel):
    id: int
    name: str
    address: Address